#take 02 numbers as input and check which one is the larger number
#if n1 is greater than n2, check whether the number is odd or even
#if it's an even number, check whether it's divisible by 4

#NESTED CONDITIONS
n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))

if n1 > n2:
    print(f"First number({n1}) is the larger number.")
    if n1 % 2 == 0:
        print(f"First number({n1}) is greater than the second number({n2}) and, is an even number.")
        if n1 % 4 == 0:
            print(f"First number({n1}) is divisible by 4.")
        else:
            print(f"First number({n1}) is not divisible by 4.")
    else:
        print(f"First number({n1}) is greater than second number({n2}) and, is an odd number.")
elif n2 > n1:
    print(f"Second number({n2}) is the larger number.")
else:
    print(f"First number({n1}) and second number({n2}) are equal numbers.")