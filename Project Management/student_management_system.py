import time
from datetime import datetime, timedelta

class Students:
    _id_counter = 1000

    def __init__(self, f_name: str, l_name: str, address: str, nic: str, nationality: str, academic_year: int):
        self.student_id = self.generate_student_id()
        self.first_name = f_name
        self.last_name = l_name
        self.address = address
        self.nic = nic
        self.nationality = nationality
        self.academic_year = academic_year

    @classmethod
    def generate_student_id(cls):
        cls._id_counter += 2
        return f"STU{cls._id_counter}"

    def calculate_age(self):
        birth_year = int(self.nic[:4])
        current_year = datetime.now().year
        return current_year - birth_year

    def get_gender(self):
        return "Female" if int(self.nic[4:7]) > 500 else "Male"

    def get_birthday(self):
        year = int(self.nic[:4])
        day_of_year = int(self.nic[4:7])
        if day_of_year > 500:
            day_of_year -= 500
        dob = datetime(year, 1, 1) + timedelta(days=day_of_year - 2)  # Fixed offset
        return dob.date()

students = {}

def add_student():
    print("\n=== Add New Student ===")
    f_name = input("Enter First Name: ")
    l_name = input("Enter Last Name: ")
    address = input("Enter Address: ")
    nic = input("Enter NIC: ")
    academic_year = int(input("Enter Academic Year: "))

    student = Students(f_name, l_name, address, nic, "Sri Lankan", academic_year)
    students[student.student_id] = student
    print(f"\n✅ Student Added Successfully! Assigned ID: {student.student_id}\n")
    time.sleep(1)

def list_students():
    if not students:
        print("\n⚠️  No students found!\n")
        return False
    print("\n--- Student List ---")
    print(f"{'ID':<10} {'First Name':<15} {'Last Name':<15}")
    print("-" * 40)
    for sid, stu in students.items():
        print(f"{sid:<10} {stu.first_name:<15} {stu.last_name:<15}")
    print("-" * 40 + "\n")
    return True

def calculate_age():
    if list_students():
        student_id = input("Enter Student ID to calculate age: ")
        if student_id in students:
            print(f"🎂 Age of {students[student_id].first_name}: {students[student_id].calculate_age()} years\n")
        else:
            print("❌ Student not found!\n")

def get_gender():
    if list_students():
        student_id = input("Enter Student ID to get gender: ")
        if student_id in students:
            print(f"🚻 Gender: {students[student_id].get_gender()}\n")
        else:
            print("❌ Student not found!\n")

def get_birthday():
    if list_students():
        student_id = input("Enter Student ID to get birthday: ")
        if student_id in students:
            print(f"🎉 Birthday: {students[student_id].get_birthday()}\n")
        else:
            print("❌ Student not found!\n")

def main():
    while True:
        print("""=============== Student Management System ===============
1. Add Student
2. Calculate Student Age
3. Get Student Gender
4. Get Student Birthday
5. List All Students
6. Exit
==========================================================""")

        try:
            choice = int(input("👉 Enter your choice: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.\n")
            continue

        if choice == 1:
            add_student()
        elif choice == 2:
            calculate_age()
        elif choice == 3:
            get_gender()
        elif choice == 4:
            get_birthday()
        elif choice == 5:
            list_students()
        elif choice == 6:
            print("\n👋 Exiting Student Management System. Goodbye!\n")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
