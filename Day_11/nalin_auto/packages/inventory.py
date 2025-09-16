cars = [
    {"id" : "1", "brand" : "Toyota", "Model" : "Supra", "country_of_origin" : "Japan","manufacture_year" : 2025, "quantity" : 5,"Price" : 50000},
    {"id" : "2", "brand" : "Nissan", "Model" : "GT R-35", "country_of_origin" : "Japan","manufacture_year" : 2025, "quantity" : 10,"Price" : 60000},
    {"id" : "3", "brand" : "Porsche", "Model" : "911 Carrera", "country_of_origin" : "Italy","manufacture_year" : 2025, "quantity" : 3,"Price" : 132000},
]

def add_to_inventory(inventory, car_id, brand, model, origin, year, quantity, price):
        for car in inventory:
            if car_id not in car["id"]:
                cars.append({"id" : car_id, "brand" : brand, "Model" : model, "country_of_origin" : origin, "manufacture_year" : year, "quantity" : quantity, "Price" : price})
                return "Car added to inventory"
            else:
                return "Car is already in the inventory"
        return None


def search_car_by_brand(brand):
    searched_items = []
    for car in cars:
        if brand == car["brand"]:
            searched_items.append(car)

    if len(searched_items) > 0:
        return searched_items

    return None

def view_inventory():
    for car in cars:
        print(car)

def remove_from_inventory(car_id):
    global cars

    cars = [car for car in cars if car["id"] != car_id]
    print(f"Car {car_id} removed from inventory")


if __name__ == "__main__":
    print(search_car_by_brand("Toyota"))
    print(add_to_inventory(cars, "4", "brand", "model", "origin", "year", "quantity", 2333))
    view_inventory()
    remove_from_inventory(1)
    view_inventory()