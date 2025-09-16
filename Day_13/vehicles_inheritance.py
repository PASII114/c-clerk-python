class Vehicles:

    def __init__(self, mode, v_type, brand, name):
        self.mode = mode
        self.type = v_type
        self.brand = brand
        self.name = name


class LandVehicles(Vehicles):

    def __init__(self, mode, v_type, brand, name, color):
        Vehicles.__init__(self, mode, v_type, brand, name)
        self.color = color

    def travel_by(self):
        print(f"A {self.type} is travel by {self.mode}")

class Cars(LandVehicles):

    def __init__(self, mode, v_type, brand, name, color, speed):
        LandVehicles.__init__(self, mode, v_type, brand, name, color)
        self.speed = speed

    def travelling(self):
        print(f"Average speed of a {self.brand} {self.name} is {self.speed}km/h")

car = Cars("Road", "car", "Lamborghini", "Aventador SVJ", "Purple", 100)

car.travelling()