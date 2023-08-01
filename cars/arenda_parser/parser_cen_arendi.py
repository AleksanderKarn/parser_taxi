import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

from arenda_avito.models import ArendaCar
from cars.arenda_parser.car_list import car_list, do_2k_list

from cars.arenda_parser.config_for_arenda_auto import url_arenda_auto

dict_data = {}
list_tiker = []
taxoparks = []


def func(arg, block, kwargs):
    taxopark = kwargs.find_element(By.TAG_NAME, 'p').text
    if taxopark in taxoparks:
        return
    taxoparks.append(taxopark)

    grafic = ['7/0', '6/1', '5/2', '2/2']
    schedule = ''

    price = block.find_element(By.CLASS_NAME, "iva-item-priceStep-uq2CQ").find_element(By.CLASS_NAME,
                                                                                 'price-root-RA1pj').text  # цена
    if price != "Бесплатно":
        price = int(price.split("₽")[0].replace(" ", "").replace("от", ""))
        if price < 1000:
            return
    elif price == "Бесплатно":
        return

    title = block.find_element(By.CLASS_NAME, "iva-item-titleStep-pdebR").find_element(By.CLASS_NAME,
                                                                                       'iva-item-title-py3i_').text  # название

    for car in car_list:
        if arg.find(car) != -1:
            if car in do_2k_list and price > 2000:
                continue
            else:

                dict_data[title] = [car, price, taxopark, arg, schedule]  # , link, placement_date, percent, uslovia]
                return





def get_content_for_page():
    count = 0
    page_count = 0
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win64",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    driver.get(url_arenda_auto)

    while True:
        block_content = driver.find_elements(By.CLASS_NAME, 'iva-item-content-rejJg')  # блок со всеми машинами страницы
        if page_count == 0:
            page_count = int(driver.find_elements(By.CLASS_NAME, 'styles-module-text-InivV')[-1].text)  # число страниц

        if count >= page_count - 1:  # условие остановки парсера
            break
        count += 1

        for block in block_content:
            description = block.find_element(By.CLASS_NAME,
                                             "iva-item-descriptionStep-C0ty1").text  # описание обьявления
            try:
                taxoparks = block.find_element(By.CLASS_NAME, 'style-root-uufhX')  # если есть название таксопарка
                func(description, block, taxoparks)
            except Exception:
                continue

        next_page = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/div[3]/div/div[2]/div[3]/div[3]/div[4]/nav/ul/li[9]/a')
        next_page.click()
        time.sleep(1)


def write_function():
    for value in dict_data.values():
        if value[0] != '':

            ArendaCar.objects.create(cars=value[0], price=value[1], taxopark=value[2], schedule=value[4], description=value[3])  # placement_date=value[6], komission_park=value[7], description=value[4] ,link=value[2], usloviya_vivoda_sredstv=value[8])
        else:
            ArendaCar.objects.create(cars='Машин из нашего автопарка нет', price=value[1], taxopark=value[2], schedule=value[4], description=value[3])


def reader():
    dict_for_read = {}
    name_companyes = []
    prices = []
    cars = []

    for i in dict_data.values():
        cars.append(i[0])
        name_companyes.append(i[2])
        prices.append(i[1])
    dict_for_read["Название таксопарка"] = name_companyes
    dict_for_read["Марки машин"] = cars
    dict_for_read["Цена в шапке объявления"] = prices
    df = pd.DataFrame(dict_for_read)
    df.to_excel('./Аренда_авито_авто.xlsx', index=False)


def _main():
    get_content_for_page()
    write_function()
    reader()
    print('конец записи')
