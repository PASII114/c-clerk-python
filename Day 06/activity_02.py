#take marks of 5 subjects
#then calculate the average of the marks
# then based on the average grade the student
# < 35 fail
# > 50 c
# >= 75 A

total_marks = []

for i in range(5):
    marks = int(input("Enter marks: "))
    total_marks.append(marks)

average_marks = sum(total_marks) // len(total_marks)

max_marks = max(total_marks)

print(f"Highest score is: {max_marks}")

if average_marks >= 75:
    print("Your grade is A. Good Job!")
elif average_marks >= 50 :
    print("Your grade is C")
elif 35 < average_marks < 50:
    print("Your grade is S")
elif average_marks >= 35:
    print("Your grade is A. Good Job!")