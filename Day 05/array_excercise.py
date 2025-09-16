#get user inputs and put those in an array
#when user finishes inserting numbers he can input 0 to exit
#get the sum of the numbers in the array

number_list = []
sum_of_numbers = 0

while True:
    numbers = int(input("Enter a number: "))

    if numbers == 0:
        break

    number_list.append(numbers)


# for number in number_list:
#     sum_of_numbers += number

print(sum(number_list)) #sum of all the items on the list
print(sum(number_list) // len(number_list)) #taking the average of the list