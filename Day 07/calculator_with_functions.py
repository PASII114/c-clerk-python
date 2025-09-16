def main():

    def addition(a, b):
        return a + b

    def substraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        return a / b

    def power(a, b):
        return a ** b

    def floor_division(a, b):
        return  a // b


    num1 = float(input("Enter the first number: "))
    ope = input("Enter the arithmatic operator: ")
    num2 = float(input("Enter the second number: "))


    if ope == "+":
        print(f"Result: {addition(num1, num2)}")
    elif ope == "-":
        print(f"Result: {substraction(num1, num2)}")
    elif ope == "*":
        print(f"Result: {multiplication(num1, num2)}")
    elif ope == "/":
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            print(f"Result: {division(num1, num2)}")
    elif ope == "**":
        print(f"Result: {power(num1, num2)}")
    elif ope == "//":
        if num2 == 0:
            print("Error")
        else:
            print(f"Result: {floor_division(num1, num2)}")

main()