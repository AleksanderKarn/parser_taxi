import pandas as pd

from cars.models import Car
from cars.parser.funk_to_parser import file_name_create, clean_table, get_data, funk, format_link
from cars.parser.setting_for_parser import URL_AUTO


def main():
    data = get_data()
    clean_table()
    link = format_link(URL_AUTO, data)
    data_list = funk(data, link)
    df = pd.DataFrame(data_list)
    file_name = file_name_create(data)
    df.to_excel(file_name)
    Car.objects.all().delete()  # Очищаем базу данных с машинами для поиска
