from unittest import result

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where --" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

task_02 = alice_in_wonderland.count("'")
print(f"Кількість одинарних лапок: {task_02}")
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea = 436402
azov_sea = 37800
total_sea = black_sea + azov_sea
print(f"Загальна площа {total_sea} км2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
sklad1_sklad2 = 250449
sklad2_sklad3 = 222950
all_gds = 375291
sklad1 = all_gds - sklad2_sklad3
sklad3 = all_gds - sklad1_sklad2
sklad2 = sklad1_sklad2 - sklad1
print(f"Склад 1: {sklad1} Склад 2: {sklad2} Склад 3: {sklad3}")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

price_per_m = 1179
months = 18
total_price = price_per_m * months
print(f"Вартість комп'ютера {total_price}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

# a)
a = 8019
b = 8
result = a % b
print(f"a) {result}")

# b)
a = 9907
b = 9
result = a % b
print(f"b) {result}")

# c)
a = 2789
b = 5
result = a % b
print(f"c) {result}")

# d)
a = 7248
b = 6
result = a % b
print(f"d) {result}")

# e)
a = 7128
b = 5
result = a % b
print(f"e) {result}")

# f)
a = 19224
b = 9
result = a % b
print(f"f) {result}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_b = 4 * 274
pizza_m = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total = pizza_b + pizza_m + juice + cake + water
print(f"Вартість замовлення {total}")



# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_ph = 232
ph_per_page = 8
page_need = total_ph // ph_per_page
rest = total_ph % ph_per_page
if rest > 0:
    page_need = page_need + 1
print(page_need)


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_per_100 = 9
volume = 48

#1)
total_fuel = (distance // 100) * fuel_per_100
print(total_fuel)

#2)
refills = total_fuel // volume
if total_fuel % volume > 0:
    refills = refills + 1
print(refills)
