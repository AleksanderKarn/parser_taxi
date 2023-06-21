import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

from arenda_avito.models import ArendaCar
from cars.arenda_parser.car_list import car_list

from cars.arenda_parser.config_for_arenda_auto import url_arenda_auto

dict_data = {}
list_tiker = []


def func(arg, block, kwargs):
    grafic = ['5/2', '2/2', '6/1', '7/0']
    schedule = ''
    cars = []
    for car in car_list:
        if arg.find(car) != -1:
            cars.append(car)

    title = block.find_element(By.CLASS_NAME, "iva-item-titleStep-pdebR").find_element(By.CLASS_NAME,
                                                                                       'iva-item-title-py3i_').text  # названи
    price = block.find_element(By.CLASS_NAME, "iva-item-priceStep-uq2CQ").find_element(By.CLASS_NAME,
                                                                                       'price-root-RA1pj').text  # цена
    link = block.find_element(By.TAG_NAME, 'a').get_attribute("href")
    taxopark = kwargs.find_element(By.TAG_NAME, 'p').text
    placement_date = block.find_element(By.CLASS_NAME, 'iva-item-dateInfoStep-_acjp').text

    for day in grafic:
        if arg.find(day) != -1:
            schedule += day + ', '
    if schedule == '':
        schedule += 'не указано'

    dict_data[title] = [cars, price, link, taxopark, arg, schedule, placement_date]


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

        if count >= page_count:
            break
        count += 1

        for block in block_content:
            description = block.find_element(By.CLASS_NAME,
                                             "iva-item-descriptionStep-C0ty1").text  # описание обьявления

            try:
                taxoparks = block.find_element(By.CLASS_NAME, 'style-root-uufhX')
                func(description, block, taxoparks)
            except Exception:
                print()

        next_page = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div[3]/div[4]/nav/ul/li[9]/a')
        next_page.click()
        time.sleep(1)


def write_function():
    for value in dict_data.values():
        cars_str = ''
        if value[0] != []:
            for i in value[0]:
                cars_str += i + ', '

            ArendaCar.objects.create(cars=cars_str, price=value[1], link=value[2]
                                     , taxopark=value[3], description=value[4], schedule=value[5],
                                     placement_date=value[6])
        else:
            ArendaCar.objects.create(cars='Машин из нашего автопарка нет', price=value[1], link=value[2]
                                     , taxopark=value[3], description=value[4], schedule=value[5],
                                     placement_date=value[6])


def reader():
    dict_for_read = {}
    name_companyes = []
    prices = []
    cars = []
    schedulers = []
    descriptions = []
    date_create = []
    for i in dict_data.values():
        name_companyes.append(i[3])
        cars = i[2]
        prices.append(i[1])
        schedulers.append(i[5])
        descriptions.append(i[4])
        date_create.append(i[6])
    dict_for_read["Название компании"] = name_companyes
    dict_for_read["Машины"] = cars
    dict_for_read["Цена"] = prices
    dict_for_read["График"] = schedulers
    dict_for_read["Описание"] = descriptions
    dict_for_read["Дата создания объявления"] = date_create

    df = pd.DataFrame(dict_for_read)
    df.to_excel('./PRIMER.xlsx', index=False)


def _main():
    get_content_for_page()
    write_function()
    reader()
    print('конец записи')
