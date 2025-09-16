#take the numbers as inputs
#take the operator which user want to perform
# then check for the operator with if condition and perform the calculation and print

no1 = float(input("Enter Number 1: "))
opa = (input("Enter Arithmetic Operator: "))
no2 = float(input("Enter Number 2: "))

if opa == "+":
    print(f"Performing Addition {no1 + no2} ")

if opa == "-":
    print(f"Performing Subtract {no1 - no2}")

if opa == "*":
    print(f"Performing Multiplication {no1 * no2}")

if opa == "/":
    if no2 == 0:
        print("error cannot be divided by 0")
    else:
        print(f"Performing Dividing  {no1 / no2}")

if opa == "**":
    print(f"Performing Power {no1 ** no2}")

if opa == "//":
    print(f"ii {no1 // no2}")

