numbers1 = [i for i in range(1, 10)]

numbers2 = numbers1[0:4]

print(numbers2)
print("#########################")


numbers3 = []

numbers3.extend(numbers1) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers3.append(numbers1) #[[1, 2, 3, 4, 5, 6, 7, 8, 9]]
numbers3.append(numbers1) #[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]

print(numbers3[0])
print(numbers3[9][0])
print(numbers3)