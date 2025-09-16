class ExampleClass:

    count = 0  #class variable

    def __init__(self, val = 1):
        self.__val = val #instance variables
        self.val2 = 10
        ExampleClass.count += 1

    def __str__(self):
        return "test"

    def say_hello(self):
        self.hello = "Hellooooooooo!!!!!!!!"

test = ExampleClass()
print(ExampleClass.count)
test2 = ExampleClass()
print(ExampleClass.count)

print(test.count)
print(test2.count)

test.z = 20
test.say_hello()
test.__val = 30

print(test.z)
print(test.__dict__)
print(ExampleClass.count)