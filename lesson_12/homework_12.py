#homework_11_1

def sum_numbers(line):
    part = line.split(",")
    numbers = map(int, part)
    return sum(numbers)

#homework_9_1


class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == 'side_a' and value <= 0 :
           raise ValueError(f'Недопустиме значення: {value} \nДовжина сторони має бути > 0. ')

        if key == 'angle_a' and (value <= 0 or value >= 180) :
            raise ValueError(f'Недопустиме значення: {value} \nКут має бути більше 0 і менше 180 градусів. ')

        if key == 'angle_a' :
            super().__setattr__('angle_b', 180 - value)

        if 'angle_b' == key:
            raise ValueError(f'Некоректний параметр {value} \nКут б має вираховуватись самостійно.')

        super().__setattr__(key, value)


#homework_5_1

def get_car_price(car):
    return car[1][4]


def search_cars(car_data, search_criteria):
    year, volume, price = search_criteria
    filtered_cars = []
    for car_name, car_info in car_data.items():
        car_colour, car_year, car_volume, car_type, car_price = car_info
        if car_year >= year and car_volume >= volume and car_price <= price:
            filtered_cars.append((car_name, car_info))
    filtered_cars = sorted(filtered_cars, key=get_car_price)
    return filtered_cars[0:5]


