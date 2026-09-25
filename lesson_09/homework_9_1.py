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


romb = Romb(115, 60)
print(romb.side_a)
print(romb.angle_a)
print(romb.angle_b)
romb.angle_a = 45
print(romb.angle_b)
# romb.angle_b = 100
# print(romb.angle_a, romb.angle_b)
"""Перевірила, що буде, якщо ввести параметр кута б вручну. 
Спочатку програма спрацьовувала і некоректний результат.
При romb.angle_a = 45 і romb.angle_b = 100 сума була б 145, а не 180.
Тому додала ще одну умову, за якою вручну змінювати параметр кута б неможна. """


