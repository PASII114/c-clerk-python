numbers = [number ** 2 for number in range(10)]

print(numbers)

numbers_divisible_by_5 = [i ** 2 for i in range(100) if i % 5 == 0]
print(numbers_divisible_by_5)