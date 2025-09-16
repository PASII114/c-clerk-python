#when a program to check if a number is divisible by 5, if its divisible print

no = int(input("Enter Number: "))

#print( no % 5 <= 0 )

if no % 5 <= 5:
    print(f"The number {no} can be divided by 5.")
else :
    print(f"The number cannot be divided by 5.")