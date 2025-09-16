import array

user_number = int(input("Enter a number: "))
print(user_number & 1)

if user_number & 1:
    print("Number is odd")
else:
    print("Number is even")
