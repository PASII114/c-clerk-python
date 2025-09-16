elements = [1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]

unique_elements = []

for number in elements:
    if number not in unique_elements:
        unique_elements.append(number)

elements = unique_elements[:]

print(elements)