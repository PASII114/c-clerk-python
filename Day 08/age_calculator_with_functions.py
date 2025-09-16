# take birth year as input
# take current year
# write a function to calculate age based on current year and birth year
#
# if age < 13
#     return "child"
# age < 20 "teen
#less than 50 "adult"
# age > 50 return senior citizen
#
# write a function to get age_status based on the age

def calculate_age(birth_year, current_year):
    return current_year - birth_year

def age_status(user_age):
    if user_age < 13:
        return "User is a Child.}"
    if user_age < 20:
        return "User is a Teen."
    if user_age < 50:
        return "User is an Adult."
    else:
        return "User is a Senior Citizen"


user_birth_year = int(input("Enter your birth year: "))
year_now = int(input("Enter the current year: "))

age = calculate_age(user_birth_year, year_now)

print(age_status(age))