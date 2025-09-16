print("*** Enter -1 to exit the programme ***")

odd_number = 0
even_number = 0

usr_input = float(input("Enter a number: "))

while usr_input != -1:
    if usr_input % 2 == 0:
        even_number = even_number + 1

    else:
        odd_number = odd_number + 1
        if usr_input ==-1:
            exit()

    usr_input = float(input("Enter a number: "))

print(f"Number of even numbers: {even_number}")
print(f"Number of odd numbers: {odd_number}")