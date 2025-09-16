import random

# print(help(random))

x = random.choices(["test", "ggg", "aaa"])

print(x)

d = {"test" : 1,
     "test2" : 2
     }
y = random.choices([x for x in d.keys()])

print(y)