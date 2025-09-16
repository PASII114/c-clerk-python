def strange_func():
    return

    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")
    print("Hello World")

print(strange_func())

def check_even_number(n):

    if n % 2 == 0:
        return "Number is Even"

    print("Function is running")

number = 2
odd_or_even = check_even_number(number)
print(odd_or_even)


def sum_of_list(number_list):
    total_sum = 0

    for num in number_list:
        total_sum += num

    return f"Total of the list is: {total_sum}"

numbers = [1, 2, 3, 4, 5, 6, 7]
final_sum = sum_of_list(numbers)

print(final_sum)