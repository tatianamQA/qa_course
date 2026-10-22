import unittest
from unittest import result

from lesson_12.homework_12 import sum_numbers, Romb, search_cars


class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers_with_correct_numbers(self):
        result = sum_numbers("1,2,3,4")
        self.assertEqual(result, 10)


    def test_sum_numbers_with_incorrect_numbers(self):
        with self.assertRaises(ValueError):
            sum_numbers("qwerty1,2,3")


    def test_sum_numbers_with_one_number(self):
        result = sum_numbers("1")
        self.assertEqual(result, 1)


    def test_sum_numbers_with_negative_numbers(self):
        result = sum_numbers("-1, 3")
        self.assertEqual(result, 2)


    def test_sum_numbers_with_empty_line(self):
        with self.assertRaises(ValueError):
            sum_numbers("")


class TestRomb(unittest.TestCase):
    def test_romb_with_correct_data(self):
        romb = Romb(10, 60)
        self.assertEqual(romb.angle_b, 120)


    def test_romb_with_change_angle_a(self):
        romb = Romb(10, 60)
        romb.angle_a = 45
        self.assertEqual(romb.angle_b, 135)


    def test_romb_with_incorrect_side(self):
        with self.assertRaises(ValueError):
            Romb(0, 60)


    def test_romb_with_incorrect_angle(self):
        with self.assertRaises(ValueError):
            Romb(15, 180)


    def test_romb_with_zero_angle(self):
        with self.assertRaises(ValueError):
            Romb(15, 0)

    def test_romb_with_setting_angle_b(self):
        romb = Romb(10, 60)
        with self.assertRaises(ValueError):
            romb.angle_b = 100


    def test_romb_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            Romb(-5, 60)


    def test_romb_with_boundary_data(self):
        romb = Romb(10, 179)
        self.assertEqual(romb.angle_b, 1)


class TestSearchCars(unittest.TestCase):
    car_data = {
        'Mercedes': ('silver', 2018, 1.8, 'sedan', 36000),
        'Audi': ('black', 2018, 2.0, 'sedan', 28000),
        'BMW': ('white', 2018, 3.0, 'suv', 90000),
        'Lexus': ('gray', 2015, 2.5, 'coupe', 35000),
        'Toyota': ('blue', 2020, 1.6, 'hatchback', 20000),
        'Honda': ('red', 2021, 1.5, 'sedan', 30000)

    }
    search_criteria = (2017, 1.6, 36000)


    def test_search_criteria(self):
        result = search_cars(self.car_data, self.search_criteria)
        expected_result = [('Toyota', ('blue', 2020, 1.6, 'hatchback', 20000)),
                           ('Audi', ('black', 2018, 2.0, 'sedan', 28000)),
                           ('Mercedes', ('silver', 2018, 1.8, 'sedan', 36000))
                           ]
        self.assertEqual(result, expected_result)


    def test_search_criteria_without_suitanle_criteria(self):
        search_criteria_new = (2017, 1.6, 15000)
        result = search_cars(self.car_data, search_criteria_new)
        expected_result = []
        self.assertEqual(result, expected_result)


    def test_search_criteria_with_len_suitable_cars(self):
        car_data = {
            'Mercedes': ('silver', 2018, 1.8, 'sedan', 36000),
            'Audi': ('black', 2018, 2.0, 'sedan', 28000),
            'BMW': ('white', 2018, 3.0, 'suv', 20000),
            'Lexus': ('gray', 2017, 2.5, 'coupe', 35000),
            'Toyota': ('blue', 2020, 1.6, 'hatchback', 20000),
            'Honda': ('red', 2021, 1.8, 'sedan', 30000)

        }
        result = search_cars(car_data, self.search_criteria)
        expected_result = 5
        self.assertEqual(len(result), expected_result)
