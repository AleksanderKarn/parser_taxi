import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

from arenda_avito.models import ArendaCar
from cars.arenda_parser.car_list import car_list

from cars.arenda_parser.config_for_arenda_auto import url_arenda_auto

dict_data = {}
list_tiker = []


def func(arg, block):

    for car in car_list:
        if arg.find(car) != -1:
            title = block.find_element(By.CLASS_NAME, "iva-item-titleStep-pdebR").find_element(By.CLASS_NAME,
                                                                                               'iva-item-title-py3i_').text  # название

            price = block.find_element(By.CLASS_NAME, "iva-item-priceStep-uq2CQ").find_element(By.CLASS_NAME,
                                                                                               'price-root-RA1pj').text  # цена
            link = block.find_element(By.TAG_NAME, 'a').get_attribute("href")


            dict_data[title] = [car, price, link]

            return 0
    return 0


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
        block_content = driver.find_elements(By.CLASS_NAME, 'iva-item-body-KLUuy')  # блок со всеми машинами страницы
        if page_count == 0:
            page_count = int(driver.find_elements(By.CLASS_NAME, 'styles-module-text-InivV')[-1].text)  # число страниц

        if count >= 1: #page_count:
            break
        count += 1

        for block in block_content:
            description = block.find_element(By.CLASS_NAME, "iva-item-descriptionStep-C0ty1").text  # описание обьявления

            func(description, block)

        next_page = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div/div[2]/div/div[2]/div[3]/div[3]/div[4]/nav/ul/li[9]/a')
        next_page.click()
        time.sleep(1)


def write_function():
    for i in dict_data.values():
        ArendaCar.objects.create(mark=i[0].split(' ')[0], model=i[0].split(' ')[1], price=i[1], link=i[2])


def _main():
    get_content_for_page()
    write_function()
    print('конец записи')