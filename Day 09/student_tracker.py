# x = 10
#
# def test():
#     global x
#     x = 15
#     print(x)
#
# test()
# print()

students = {}


def add_student_details(student, name, age, address, contact, student_id):

    if student_id not in student:
        student[student_id] = {
            "name" : name,
            "age" : age,
            "address" : address,
            "contact" : contact
        }
    else:
        print("Student Id already exists.")

def view_student_details(student, student_id):
    if student_id in student:
        for key, val in student[student_id].items():
            print(f"{key}  - {val}")
    else:
        print("Student not found.")

def delete_student_detail(student, student_id):
    if student_id in student:
        del student[student_id]
        print(f"Details of Student {student_id} deleted successfully.")
        print(student)
    else:
        print("Student not found.")

def edit_mobile_no(student, student_id, contact):
    if student_id in student:
        student[student_id]["contact"] = contact
        print("Contact updated successfully.")
    else:
        print("Student not found.")

def view_all_students(student):
    for student_id in student.keys():
        print(f"Student Id - {student_id} : Student name - {student[student_id]["name"]}")


def add_marks(student, student_id):

    if student_id in student:
        try:
            science = int(input("Enter Science Marks: "))
            maths = int(input("Enter Maths Marks: "))
            english = int(input("Enter English Marks: "))


            student[student_id]["Marks"] = {
                "science": science,
                "maths": maths,
                "english": english
            }

            print("Marks added successfully")
        except ValueError:
            print("Please enter a valid integer value")
            add_marks(student, student_id)

    else:
        print("Student not found")


def view_marks(student, student_id):
    if student_id in student:
        if "Marks" in student[student_id]:
            for key, val in student[student_id]["Marks"].items():
                print(f"{key}  - {val}")
        else:
            print("Add marks before viewing marks.")

    else:
        print("Student not found")


def get_grade(grade):
    if grade > 75:
        return "A"
    elif grade > 60:
        return "B"
    elif grade > 30:
        return "C"
    else:
        return "F"


def average_marks(student):
    for key, val in students.items():
        if "Marks" in val:
            total = 0
            for marks in val["Marks"].values():
                total += marks
            print(f"{val["name"]} average marks - {total // 3}")
            print(f"Your average grade is {get_grade(total // 3)}")



def main():
    print("==================Menu==================")
    print("""1. Add Student student
2. View Student Details
3. Delete Student Detail
4. Edit Mobile Number
5. View names of all the students
6. Add Marks
7. View Marks
8. View Average Marks""")

    choice = int(input("Select your option(1-2): "))

    if choice == 1:


        input_id = int(input("Enter Student ID: "))
        input_name = input("Enter Student Name: ")
        input_age = int(input("Enter Student age: "))
        input_address = input("Enter Student Address: ")
        input_phone_no = input("Enter Student Mobile No: ")

        add_student_details(students, name = input_name, age = input_age, address = input_address, contact = input_phone_no, student_id = input_id)
        print(students)

    elif choice == 2:
        stu_id = int(input("Enter Student Id: "))

        view_student_details(students, student_id = stu_id)

    elif choice == 3:
        print(students)

        stu_id = int(input("Enter the Student id you want to delete: "))

        delete_student_detail(students, student_id = stu_id)

    elif choice == 4:
        stu_id = int(input("Enter Student Id: "))
        phone_no = input("Enter the Mobile Number: ")

        edit_mobile_no(students, student_id = stu_id, contact = phone_no)
        print(students)

    elif choice == 5:
        view_all_students(students)

    elif choice == 6:
        stu_id = int(input("Enter the student id: "))

        add_marks(students, student_id = stu_id)

    elif choice == 7:
        stu_id = int(input("Enter the student id: "))

        view_marks(students, student_id = stu_id)

    elif choice == 8:
        average_marks(students)

    else:
        print("Enter a valid choice.")

while True:
    main()