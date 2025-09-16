items = []

# for i in range(5):
#     items.append(i + 1)
#
# print(items)

for i in range(5):
    items.insert(0, i + 1)

print(items)

x = 10
y = 20

x, y = y, x

print(x, y)

print("hello" [2])