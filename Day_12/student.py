class Student:

    def __init__(self, name, age, institute):
        self.name = name
        self.age = age
        self.institute = institute
        print("Constructor called")

    def eat(self):
        print(f"Im eating {self.name} {self.age}")

    def sleep(self):
        print(f"Im sleeping {self.name} {self.age}")

    def show_details(self):
        print(f"Name - {self.name}\nAge - {self.age}\nInstitute - {self.institute}")

    def compare(self, std):
        return self.name == std.name


#Creating an Object / Instance

student1 = Student("Pasindu", 22, "C-clarke") #Objects are created in heap(RAM)
student2 = Student("Rashmika", 22, "C-clarke")

print(type(student1))

print(student1)
print(student2)

student1.show_details()
student2.show_details()

if student1.compare(student2):
    print("Students are same")
else:
    print("Students are not same")