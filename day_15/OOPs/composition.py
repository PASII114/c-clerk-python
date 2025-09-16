from filecmp import clear_cache


class Engine:

    def __init__(self, engine_no: str, horse_power: int, capacity: str):
        self.engine_no = engine_no
        self.horse_pw = horse_power
        self.capacity = capacity

    def start(self) -> None:
        print("Engine Starting")


class Car:

    def __init__(self, brand: str, engine: Engine):
        self.brand = brand
        self.engine = engine

    def print_car_info(self) -> None:
        print(f"car brand {self.brand} Engine capacity {self.engine.capacity}")


car = Car("Lamborghini", Engine("qihebd1314", 1000, "2500CC"))
car.print_car_info()