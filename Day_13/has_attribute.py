class Classy:

    im_classy = "Classy"

    def __init__(self):
        self.a = "ABCDEF"
        self.b = 30

    def say_hello(self):
        print("Hello World")

    def top_g(self):
        self.g = "What color is ur Bugatti??"
        self.say_hello()

classy_object = Classy()

print(classy_object.a)

classy_object.top_g()

print(hasattr(classy_object, 'g'))

print(classy_object.g)

print(classy_object.__dict__)
if 'g' in classy_object.__dict__:
    print("Yes Im in")