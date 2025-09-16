two_dim_array = [["x", "x", "x"],
                 ["x", "x", "x"],
                 ["x", "x", "x"],
                 ["x", "x", "x"]]

two_dim_array[1][1] = "b"

print(two_dim_array)

for element in two_dim_array:
    print(element)

    for i in element:
        print(i)