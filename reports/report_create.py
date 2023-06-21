from arenda_avito.models import ArendaCar


def dserhgareh():
    cars = ArendaCar.objects.all()

    car_dict = {}

    for car in cars:
        mark = car.mark
        model = car.model
        taxopark = car.taxopark
        key = mark + model

        price = ''.join(car.price.split('₽')[0]).replace('от', '').replace(' ', '')

        if len(price) < 5 and len(price) >= 4:
            price = int(price)
            if key in car_dict:
                car_dict[key].append(price)
            else:
                values = []
                values.append(price)
                car_dict[key] = values

    for i in car_dict.items():
        # print(i)
        print(f"{i[0]}: цена аренды от {min(i[1])} до {max(i[1])}")
        # print(int(sum(i)/len(i)))
        print('-------------------')


