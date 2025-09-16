class Animal:

    def __init__(self, scientific_name, color):
        self.scientific_name = scientific_name
        self.color = color

    def eat(self):
        print(f"{self.scientific_name} is eating.")

    def sleep(self):
        print(f"{self.scientific_name} is sleeping.")

class Mammal(Animal):

    def __init__(self, name, color, breed):
        Animal.__init__(self, name, color)
        self.breed = breed

    def drinking_milk(self):
        print(f"{self.scientific_name} which is a {self.breed} is drinking Milk.")

class Dog(Mammal):

    def __init__(self, color, breed, tail):
        Mammal.__init__(self,"Canis Lupus Familiaris", color, breed)
        self.tail = tail

dog = Dog( "white", "husky", True) #inctance Instantiate

dog.eat()
dog.drinking_milk()

print(isinstance(dog, Mammal))
print(issubclass(Mammal, Animal))