class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def change_average_score(self, new_average_score):
        self.average_score = new_average_score

    def show_info(self):
        print(f"Full information about student.\n"
              f"Full name: {self.name} {self.surname}\n"
              f"Age: {self.age}\n"
              f"Average score: {self.average_score}\n"
              )


student = Student('Tetiana', 'Medvedchuk', 24, 98.3)
student.show_info()
student.change_average_score(100)
student.show_info()
