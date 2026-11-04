import functools
import logging

logging.basicConfig(level=logging.INFO)


def log_cals_and_results(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Виклик {func.__name__}, args = {args}, kwargs = {kwargs} ")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} повернула: {result}")
        return result
    return wrapper


def catch_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except StopIteration:
            raise
        except Exception as error:
            logging.error(f"Помилка в {func.__name__}: {type(error).__name__}: {error}")
            return None
    return wrapper


@log_cals_and_results
def even_numbers_to_n(limit):
    count = 0
    while count <= limit:
        yield count
        count += 2

print(list(even_numbers_to_n(10)))
print(list(even_numbers_to_n(100)))


@catch_exceptions
def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


print(list(fibonacci_generator(10)))


class ReversIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.current = len(self.numbers) - 1


    def __iter__(self):
        return self

    @log_cals_and_results
    def __next__(self):
        if self.current >= 0:
            number = self.numbers[self.current]
            self.current -= 1
            return number
        else:
            raise StopIteration

print(list(ReversIterator([1, 2, 3, 4])))


class EvenNumsIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0


    def __iter__(self):
        return self

    @catch_exceptions
    def __next__(self):
        if self.current <= self.limit:
            number = self.current
            self.current += 2
            return number
        else:
            raise StopIteration

print(list(EvenNumsIterator(16)))


@catch_exceptions
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))

