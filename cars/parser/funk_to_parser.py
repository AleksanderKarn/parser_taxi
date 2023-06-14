import datetime
from pathlib import Path

import requests
import sys
import subprocess
from cars.models import Car
from cars.parser.setting_for_parser import header, URL
from list_auto.models import CarList


def clean_table():
    CarList.objects.all().delete()


def car_data_create(data):
    car_data = []
    for offer in data:
        car_dict = {}
        price = offer["price_info"]["RUR"]
        name = offer["vehicle_info"]["model_info"]["name"]
        mark = offer["vehicle_info"]["mark_info"]["name"]
        mileage = offer["state"]["mileage"]
        year = offer["documents"]["year"]
        body_type = offer["vehicle_info"]["configuration"]["human_name"]
        volume = offer["vehicle_info"]["tech_param"]["human_name"]
        car_dict["mark"] = mark
        car_dict["name"] = name
        car_dict["year"] = year
        car_dict["body_type"] = body_type
        car_dict["volume"] = volume
        car_dict["mileage"] = mileage
        car_dict["price"] = price
        car_data.append(car_dict)
    return car_data


def file_name_create(data_dict: dict) -> str:
    now = datetime.datetime.now()
    output = subprocess.check_output(r'powershell -command "[Environment]::GetFolderPath(\"Desktop\")"')
    path = output.decode().strip()
    file_name = data_dict['mark'] + '_' + data_dict['model'] + '_' + str(data_dict['year_from'])
    date = str(now.isoformat()).split('.')[0].replace('-', '_').replace(':', '_').replace('T', '_')
    file_name = f'{path}/Parser_data/{date}_{file_name}.xlsx'
    (Path.home() / "Desktop" / "Parser_data").mkdir(parents=True, exist_ok=True)
    return file_name


def format_body_str(body):
    row = "{"
    for i in body.items():
        row += '"' + i[0] + '"' + ':'
        if type(i[1]) is str:
            row += '"' + i[1] + '"'
        elif type(i[1]) is list:
            for n in i[1]:
                if type(n) is dict:
                    row += '[{'
                    count = 1
                    for j in n.items():
                        if count < len(n.items()):
                            row += '"' + j[0] + '"' + ':' + '"' + j[1] + '"' + ','
                        else:
                            row += '"' + j[0] + '"' + ':' + '"' + j[1] + '"' + '}]'
                        count += 1
                else:
                    row += '[' + str(n) + ']'
        else:
            row += str(i[1])
        row += ","
    row = row[:-1] + '}'
    return row


def format_link(url, data):
    link = f'{url}{data["mark"]}/{data["model"]}/all/?year_from={data["year_from"]}&km_age_to={data["km_age_to"]}'
    return link


def fetch(url, params):
    headers = params["headers"]
    body = params["body"]
    method = params["method"]
    if method == "POST":
        return requests.post(url, headers=headers, data=body)
    if method == "GET":
        return requests.get(url, headers=headers)


def get_data() -> dict:
    car = Car.objects.all().first()
    data_dict = {}
    year_from = car.year_from
    km_age_from = car.mileage_from
    km_age_to = car.mileage_to
    mark = car.mark
    model = car.model
    data_dict['year_from'] = year_from
    data_dict['km_age_from'] = km_age_from
    data_dict['km_age_to'] = km_age_to
    data_dict['mark'] = mark
    data_dict['model'] = model
    print("Взял данные авто для поиска")
    return data_dict


def funk(data_dict: dict, link: str) -> list:
    paginate = 1
    _data_list = []

    body = {
        "category": "cars",
        "section": "all",
        "year_from": data_dict['year_from'],
        "year_to": 2023,
        "km_age_from": data_dict['km_age_from'],
        "km_age_to": data_dict['km_age_to'],
        "catalog_filter": [
            {
                "mark": data_dict['mark'].upper(),
                "model": data_dict['model'].upper()
            }
        ],
        "page": paginate,
        "geo_id": [1]
    }
    while True:
        res = format_body_str(body)
        header["body"] = res
        header["headers"]["x-retpath-y"] = link
        header["headers"]["Referer"] = link
        paginate += 1

        body["page"] = paginate
        car = fetch(URL, header)
        offers = car.json()["offers"]
        if len(offers) == 0:
            break
        _data_list += car_data_create(offers)

    for _dict in _data_list:
        CarList.objects.create(mark=_dict['mark'], model=_dict['name'], year_from=_dict['year'],
                               mileage=_dict['mileage'], price=_dict['price'], body_type=_dict['body_type'],
                               volume=_dict['volume'])
    return _data_list