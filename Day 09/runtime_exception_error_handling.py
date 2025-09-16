try:
    user_input = int(input("Enter an integer: "))
    print(user_input)
    print(user_input + "Hello World")

except ValueError:# invalid value as an input
    print("Only enter numeric values")
except TypeError:
    print("Cannot add integers and strings")
finally:# even if an error occurred or not, this sections is executing
    print("Finally block executed")


try:
    user_input = int(input("Enter an integer: "))
    print(user_input)
    print(user_input + "Hello World")

except (ValueError, TypeError):
    print("Value error or type error occurred")
finally:# even if an error occurred or not, this sections is executing
    print("Finally block executed")