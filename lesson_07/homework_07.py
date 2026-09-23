# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25

            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# Перевірка
multiplication_table(6)
# має бути брейк на 6*4, бо 6x5 > 25
# 6x1=6
# 6x2=12
# 6x3=18
# 6x4=24


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_function(a, b):
    return a + b


print(sum_function(3, 2))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

lst1 = [1, 2, 3, 4, 5]
lst2 = [2, 4, 6]  #4
lst3 = [1, 2]
lst4 = []


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


print(calculate_average(lst2))
print(calculate_average(lst1))
print(calculate_average(lst3))
# print(calculate_average(lst4)) - ZeroDivisionError: division by zero

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_text(text):
    return text[::-1]


print(reverse_text("Hello, world!"))
# print(reverse_text(""))  повертає пустий рядок, без помилки


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

long_lst = ['cat', 'elephant', 'dog']
long_lst_1 = ['cat', 'dog']
long_lst_2 = []


def longest_word(words):
    return max(words, key=len)


print(longest_word(long_lst))
print(longest_word(long_lst_1))
# print(longest_word(long_lst_2))   ValueError: max() iterable argument is empty - помилка при пустому лісті


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7

lst_from_6_4 = [1, 2, 3, 4, 5, 6, 4.0, -1, -6, 2.5, 0, 'abc']


def even_numbers_sum(items):
    """Функція, яка рахує суму всіх парних чисел у лісті(задача з дз 6.4)
    Функція спочатку перебирає всі елементи лісту(можуть бути будь-які),
    відбирає ті, які підходять по параметрах, а саме:
    є цілими числами "type(item) == int" і є парними "item % 2 == 0"
    Потім відібрані числа сумуються задопомогою лічильника "total"
    Повертає інт(число) - суму всіх знайдених парних чисел, всі інші елеенти ігноруються."""
    total = 0
    for item in items:
        if type(item) == int and item % 2 == 0:
            total += item
    return total


print(even_numbers_sum(lst_from_6_4))


# task 8
all_items = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']


def get_strings(items):
    """Функція, що витягує з першоджерела(ліста) лише типи данних стрінг і формує їх в новий ліст
    параметри - дані будь-якого типу
    повертає - новий ліст лише зі стрінгами"""
    strings_list = []
    for item in items:
        if type(item) == str:
            strings_list.append(item)
    return strings_list


print(get_strings(all_items))


# task 9
""" Задача ДЗ 3, Такса 9
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

def calculate_pages(total_photos, photos_per_page):
    """Функція рахує скільки потрібно сторінок для певної к-сті фото, при певному обмеженні к-сті фото на
    одній сторінці.
    Параметр total_photos - задана загальна к-сть фото
    Параметр photos_per_page - кількість фото на одній сторінці
    Повертає кількість потрібних сторінок в альбомі - pages_need"""

    pages_need = total_photos // photos_per_page
    if total_photos % photos_per_page > 0:
        pages_need = pages_need + 1
    return pages_need


print(calculate_pages(232, 8))
print(calculate_pages(233, 8))
print(calculate_pages(0, 8))
# print(calculate_pages(232, 0))  ZeroDivisionError: division by zero - помилка через ділення на 0


# task 10

test_text = "By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher." # 5


def count_cap_words(text):
    """ ДЗ 3, такса 5
    Функція рахує к-сть слів,що розпочинаються на велику літеру
    параметр - text(str) заданий текст
    повертає int, кількисть слів"""
    count_cap = 0
    words = text.split()
    for word in words:
        if word[0].isupper():
            count_cap += 1
    return count_cap


print(count_cap_words(test_text))
print(count_cap_words("Hello World"))
print(count_cap_words(""))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""