# ЗАВДАННЯ 1
from abc import ABC, abstractmethod


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):

    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


# manager_1 = Manager('Anna', 20000, 'QA')
# print(manager_1.name)

# print(TeamLead.__mro__)

# assert hasattr(team_lead_1, 'department'), "У ТЛ немає атребуту 'department'"
# assert hasattr(team_lead_1, 'programming_language'), "У ТЛ немає атребуту 'programming_language'"
# assert hasattr(team_lead_1, 'team_size'), "У ТЛ немає атрибуту 'team_sizzze'"

def test_team_leads_all_fields():
    team_lead_1 = TeamLead('Anna', 20000, 'QA', 'c#', 5)
    team_leads_all_fields = ('name', 'salary', 'department', 'programming_language', 'team_size')
    for field in team_leads_all_fields:
        assert hasattr(team_lead_1, field), f"У TL немає атребуту {field}"
test_team_leads_all_fields()
# якщо додати 'team_sizzze' наприклад в тюпл, - AssertionError: У TL немає атребуту team_sizzze

# ЗАВДАННЯ 2
class Figure(ABC):
    @abstractmethod
    def calculating_area(self):
        pass

    @abstractmethod
    def calculating_perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def calculating_area(self):
        return self.__side_length ** 2

    def calculating_perimeter(self):
        return self.__side_length * 4

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def calculating_perimeter(self):
        return self.__a + self.__b + self.__c

    def calculating_area(self):
        p = self.calculating_perimeter() / 2
        return (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5


class Rombus(Figure):
    def __init__(self, d1, d2):
        self.__d1 = d1
        self.__d2 = d2

    def calculating_area(self):
        return (self.__d1 * self.__d2) / 2

    def calculating_perimeter(self):
        side = ((self.__d1 / 2) ** 2 + (self.__d2 / 2) ** 2) ** 0.5
        return side * 4

figures = [Square(15), Triangle(8,9,6), Rombus(12,15)]
for figure in figures:
    name = figure.__class__.__name__
    area = figure.calculating_area()
    perimeter = figure.calculating_perimeter()
    print(f"{name}: площа = {area:.1f}, периметр = {perimeter:.1f}")