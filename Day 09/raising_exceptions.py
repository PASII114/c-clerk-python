def check_age(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less than zero") #raising exceptions in a functions
    else:
        print(age)

try:
    check_age(0)
except ValueError:
    print("An error occurred")