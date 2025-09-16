unsorted_list = [4, 3, 5, 2, 1, 10, 2, 7]
arr_length = len(unsorted_list)

for i in range(arr_length - 1 ):# for not go out of range of the list
    for j in range(arr_length - i - 1):

        if unsorted_list[j] > unsorted_list[j + 1]:
            unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

print(unsorted_list)