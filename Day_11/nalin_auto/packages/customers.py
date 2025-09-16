customers = [
    {"nic" : "1", "name" : "Sanjana Adithya", "phone" : "0712687889", "order"
     : [ {"id" : "3", "brand" : "Porsche", "Model" : "911 Carrera", "country_of_origin" : "Italy","manufacture_year" : 2025, "quantity" : 3,"Price" : 132000}]}
]

def add_customers(customer_list, nic, name, phone_no, order):
    for customer in customer_list:
        if nic not in customer["nic"]:
            customer_list.append({"nic" : nic, "name" : name, "phone" : phone_no, "order" : order})
            return "Customer Added Successfully"
        else:
            return "Customer Already Exists."
    return None

def view_all_customers():
    for customer in customers:
        print("Customers")
        print("==============================")
        print(f"NIC - {customer["nic"]}\nName - {customer["name"]}\nPhone - {customer["phone"]}\nOrder - {customer["order"]}")
        print("------------------------------")

def customer_order(order_id, car_model, car_price):
    for orders in customers:
        if order_id not in orders["order"]:
            orders["order"].append(order_id, car_model, car_price)
            return "Order Added Successfully"
        else:
            return "Order Already Exists"

    return None

print(add_customers(customers, "2", "khbfib", 12345, {"id" : "3", "brand" : "Porsche", "Model" : "911 Carrera", "country_of_origin" : "Italy","manufacture_year" : 2025, "quantity" : 3,"Price" : 132000}))
view_all_customers()