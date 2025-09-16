#Take the principal
# intrest percentage
# for how many years


principal_amount = int(input("Enter Principal Amount"))
intrest_percentage = int(input("Enter Intrest Percentage "))
years = int(input("How Many Years"))

intrest = principal_amount * intrest_percentage/100 * years

print(f"Your Annual Intrest", intrest )

