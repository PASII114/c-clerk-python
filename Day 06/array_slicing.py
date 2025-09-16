numbers = [1, 2, 3, 4, 5, 6, 7]

numbers2 = numbers[:] #[start:end] [0:7]

numbers[0] = 100

print(numbers2)

numbers_0_to_3 = numbers[0:3]

print(numbers_0_to_3)

last_element = numbers[-1:]#access the last element
print(last_element)