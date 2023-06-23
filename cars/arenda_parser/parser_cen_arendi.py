import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

from arenda_avito.models import ArendaCar
from cars.arenda_parser.car_list import car_list

from cars.arenda_parser.config_for_arenda_auto import url_arenda_auto, list_usloviya_viplat

dict_data = {}
list_tiker = []

def get_uslovia_viplat(world, arg):
    count = 0
    x = 0
    y = 0
    if arg.find(world) != -1:
        while True:
            index_one = arg[arg.find(world) - count]
            if index_one == '.' or index_one == '!' or index_one == ';':
                x = arg.find(world) - count + 2
                count = 1
                while True:
                    index_two = arg[arg.find(world) + count]
                    if index_two == '.' or index_one == '!' or index_one == ';':
                        y = arg.find(world) + count + 2
                        break
                    else:
                        count += 1
                break
            else:
                count += 1

    print(f'Условия: {arg[x:y]}')
    return arg[x:y]

def create_uslovia(arg):
    for world in list_usloviya_viplat:
        uslovia = get_uslovia_viplat(world, arg)
        if uslovia != '':
            if uslovia == 'Безопасный Выв' or uslovia == 'Выв':
                return 'Безопасный Вывод Денежных средств Ежедневно!'
            return uslovia
    return '-'


def func(arg, block, kwargs):
    grafic = ['5/2', '2/2', '6/1', '7/0']
    schedule = ''
    percent = '-'
    cars = []
    for car in car_list:
        if arg.find(car) != -1:
            cars.append(car)

    title = block.find_element(By.CLASS_NAME, "iva-item-titleStep-pdebR").find_element(By.CLASS_NAME,
                                                                                       'iva-item-title-py3i_').text  # названи
    price = block.find_element(By.CLASS_NAME, "iva-item-priceStep-uq2CQ").find_element(By.CLASS_NAME,
                                                                                       'price-root-RA1pj').text  # цена

    percent_comission = arg.find('%')

    if arg[percent_comission - 1].isdigit():


        if arg[percent_comission - 1] != ' ' and percent_comission != -1 and arg[percent_comission - 1] != '0' and \
                (arg.find('Комиссия') != -1 or arg.find('комиссия') != -1):

            if arg[percent_comission - 2] == ',' or arg[percent_comission - 2] == '.':
                percent = arg[percent_comission - 3] + ',' + arg[percent_comission - 1] + '%'
            else:
                percent = arg[percent_comission - 1] + '%'
        elif arg[percent_comission - 1] == ' ' and percent_comission != -1 and arg[percent_comission - 2] != '0' and\
                (arg.find('Комиссия') != -1 or arg.find('комиссия') != -1):

            if arg[percent_comission - 3] == ',' or arg[percent_comission - 2] == '.':
                percent = arg[percent_comission - 4] + ',' + arg[percent_comission - 2] + '%'
            else:
                percent = arg[percent_comission - 2] + '%'

    uslovia = create_uslovia(arg)

    link = block.find_element(By.TAG_NAME, 'a').get_attribute("href")
    taxopark = kwargs.find_element(By.TAG_NAME, 'p').text
    placement_date = block.find_element(By.CLASS_NAME, 'iva-item-dateInfoStep-_acjp').text

    for day in grafic:
        if arg.find(day) != - 1:
            schedule += day + ', '
    if schedule == '':
        schedule += 'Граффик не указан'

    dict_data[title] = [cars, price, link, taxopark, arg, schedule, placement_date, percent, uslovia]


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

        if count >= 10: #page_count:
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
                                     placement_date=value[6], komission_park=value[7], usloviya_vivoda_sredstv=value[8])
        else:
            ArendaCar.objects.create(cars='Машин из нашего автопарка нет', price=value[1], link=value[2]
                                     , taxopark=value[3], description=value[4], schedule=value[5],
                                     placement_date=value[6], komission_park=value[7], usloviya_vivoda_sredstv=value[8])


def reader():
    dict_for_read = {}
    name_companyes = []
    prices = []
    cars = []
    schedulers = []
    descriptions = []
    date_create = []
    percents = []
    uslovia = []
    for i in dict_data.values():
        name_companyes.append(i[3])
        cars = i[2]
        prices.append(i[1])
        schedulers.append(i[5])
        descriptions.append(i[4])
        date_create.append(i[6])
        percents.append(i[7])
        uslovia.append(i[8])
    dict_for_read["Название компании"] = name_companyes
    dict_for_read["Машины"] = cars
    dict_for_read["Цена"] = prices
    dict_for_read["График"] = schedulers
    dict_for_read["Описание"] = descriptions
    dict_for_read["Дата создания объявления"] = date_create
    dict_for_read["Комиссия парка"] = percents
    dict_for_read["Условия выплат"] = uslovia

    df = pd.DataFrame(dict_for_read)
    df.to_excel('./PRIMER.xlsx', index=False)


def _main():
    get_content_for_page()
    write_function()
    reader()
    print('конец записи')
