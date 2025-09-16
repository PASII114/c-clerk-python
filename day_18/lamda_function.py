
def add(x, y):
    return x + y


add_two_num = lambda x,y : x + y #giving a name to the anonymous lambda functions

print(add_two_num(10 ,20))

print((lambda x,y : x * y)(20, 30)) #Writing anonymous functions

math_operators = {
    "Addition" : lambda x , y : x + y,
    "Substraction" : lambda x,y : x - y,
    "Multiply" : lambda x,y : x * y,
}

for key, val in math_operators.items():
    print(f"Operations - {key} |  val - {val(20, 10)}")

print((lambda x : x % 2 == 0)(20))

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x : x * 2, numbers) )

filter_num = list(filter(lambda x : x % 2, numbers))

print(doubled)
print(filter_num)
