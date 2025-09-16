number_list = [ [['*' for _ in range(1, 10)] for _ in range(2, 20) ] ]

for star1 in number_list:
    print(star1)

    for star2 in star1:
        print(star2)

        for i in star2:
            print(i)


# ###For access each element in the first list
# for i in range(len(number_list)):
#     for j in range(len(i)):
#         for z in range(len(j)):
#             print(number_list[i][j][z])

three_dim_array = [
    [
        ['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']
    ],
    [
        ['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']
    ],
    [
        ['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']
    ]
]

print("============================================================")
print(three_dim_array[0][0][0])

for i in three_dim_array:
    print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)