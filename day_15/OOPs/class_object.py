from typing import List
from typeguard import typechecked

class Student:

    def __init__(self, student_id :str, name :str, age :int, grades :List[int]):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = grades

    def __eq__(self, obj2): #overriding equal method in object class to define equality
        return self.name == obj2.name

    def add_grades(self, grade) -> None:
        self.grades.append(grade)

    def get_average(self) -> float:
        if not self.grades:
            return 0.0

        return sum(self.grades) / len(self.grades)


student1 = Student("001", "Pasindu", 22, [22, 35, 40])
student2 = Student("001", "Pasindu", 22, [22, 35, 40])

if student1 == student2:
    print("yes, equal")