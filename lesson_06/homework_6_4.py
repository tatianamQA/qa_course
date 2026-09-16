# спосіб 1 - перевірка кожного числа в лісті і підрахунок суми одразу
lst_1 = [1, 2, 3, 4, 5, 6, 4.0, -1, -6, 2.5, 0, 'abc']       # додала стрінгу для перевірки
total = 0
for item in lst_1:
    if type(item) == int and item % 2 == 0:
        total += item
print(total)

# спосіб 2 - складання лісту2 з відібраних парних чисел і складання суми після уже з лісту2
lst_2 = []
for item in lst_1:
    if type(item) == int and item % 2 == 0:
        lst_2.append(item)
print(lst_2)
print(sum(lst_2))

