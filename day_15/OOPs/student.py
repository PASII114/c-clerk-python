from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    student_id: str
    name: str
    age: int
    grades: List[int]

    def __eq__(self, obj2):  # overriding equal method in object class to define equality
        return self.name == obj2.name

    def add_grades(self, grade) -> None:
        self.grades.append(grade)

    def get_average(self) -> float:
        if not self.grades:
            return 0.0

        return sum(self.grades) / len(self.grades)

    def add_name(self, name) -> None:
        self.name = name

student = Student("001", "Student", 22, [13])
student.add_name("Pasindu")

print(student)