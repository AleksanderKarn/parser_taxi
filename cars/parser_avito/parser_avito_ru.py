import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

from cars.parser.funk_to_parser import get_data
from list_auto_avito.models import CarListAvito
from .setting_for_avitoparser import url

page = 0  # Текущая страница
page_count = 0  # Всего страниц


def get_url(url, data) -> list:
    global page
    data_for_url = []
    res = f'{url}{data["mark"]}/{data["model"]}/?cd=1&p={page}'
    data_for_url.append(res)
    data_for_url.append(data["year_from"])
    data_for_url.append(data["km_age_from"])

    return data_for_url


def write_by_database(block_kontent, _year, _mileage):
    print('работа функции записи в базу')
    for car in block_kontent:
        title = car.find_element(By.CLASS_NAME, 'iva-item-title-py3i_')
        price = car.find_element(By.CLASS_NAME, "price-price-JP7qe")
        description = car.find_element(By.CLASS_NAME, "iva-item-autoParamsStep-WzfS8").text.strip().split(',')
        mark = title.text.split(' ')[0]
        model = title.text.split(' ')[1].split(',')[0]
        year = title.text.split(',')[1].strip()
        price = ''.join(price.text.split(' ')[:-1])
        if len(description) > 4:
            mileage = ''.join(description[0][:-2].split(' '))
        else:
            mileage = 0
        volume = description[-4].strip()
        body_type = description[-3].strip()
        if str(mileage).isdigit():
            if int(year) >= _year and int(mileage) >= _mileage:
                CarListAvito.objects.create(mark=mark, model=model, year_from=int(year),
                                            mileage=int(mileage), price=int(price), body_type=body_type,
                                            volume=volume)

    print('==============================')
    print(f"Запись закончена стр.{page}")
    print('==============================')


def connector(url, year, mileage):
    global page, page_count
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win64",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    if page == 0:
        driver.get(url)
        try:
            a = driver.find_elements(By.CLASS_NAME, "suggest-input-rORJM")
            a[0].send_keys(year)
            a[2].send_keys(mileage)
            time.sleep(1)
        except Exception as e:
            print(e)
            return 0


        while True:
            try:
                b = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[1]/div/div[2]/div[3]'
                                        '/div/button[1]')  # кнопка поиска у фильтра
                b.click()
                break
            except Exception as e:
                print(e)
                continue

        pages = driver.find_element(By.CLASS_NAME, 'button-textBox-_SF60').text.split(' ')[1]

        if pages != 'не':
            pages = int(pages)
        else:
            return 0

        if pages % 50 == 0:
            page_count = pages // 50
        else:
            page_count = pages // 50 + 1
        print(f'Колличество страниц всего: {page_count}')
        if page_count > 7:
            p = 9
        elif pages < 50:
            p = 2
        else:
            p = page_count + 2
        block_kontent = driver.find_elements(By.CLASS_NAME,
                                             "iva-item-body-KLUuy")  # Все карточки товаров на странице
        page += 1
        if p != 2:
            write_by_database(block_kontent, year, mileage)
            next = driver.find_element(By.XPATH,
                                       f'//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[4]/nav/ul'
                                       f'/li[{p}]/a')
            next.click()
        print('Блок зкончен')

        while True:
            if page > page_count and page_count != 0:
                page = 0
                page_count = 0
                break
            page += 1
            try:
                block_kontent = driver.find_elements(By.CLASS_NAME,
                                                     "iva-item-body-KLUuy")  # Все карточки товаров на странице

                write_by_database(block_kontent, year, mileage)  # запись результата в базу данных

                if page != page_count and p != 2:
                    next = driver.find_element(By.XPATH,
                                               f'//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[4]/nav/ul'
                                               f'/li[{p}]/a')
                    next.click()
            except Exception as e:
                print(e)

    return 0


def _input():
    data = get_data()  # данные авто для поиска в формате словаря
    url_avito = get_url(url, data)
    connector(url_avito[0], url_avito[1], url_avito[2])

    print('Работа парсера Окончена')


