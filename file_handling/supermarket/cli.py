import time

from models import OrderItem, Order, Customer, Product
from repositories import InMemoryProductRepository, InMemoryCustomerRepository, InMemoryOrderRepository
from service import SupermarketService, SupermarketError

supermarket_service = SupermarketService(InMemoryProductRepository(), InMemoryCustomerRepository(), InMemoryOrderRepository())

def add_product():
    try:
        product_id = input("Enter Product Id: ")
        product_name = input("Enter Product name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter quantity: "))

        supermarket_service.add_products(product_id, product_name, price, quantity)
        print(f"Product {product_name} Added Successfully")

    except ValueError as e:
        print("Type Error Occurred " + str(e))

    except SupermarketError as s:
        print(s)

def add_customer():
    try:

        customer_id = input("Enter customer id: ")
        name = input("Enter Customer name: ")
        email = input("Enter Customer Email: ")
        phone = input("Enter Customer Mobile No: ")

        supermarket_service.add_customer(customer_id, name, email, phone)
    except ValueError as e:
        print("Type Error Occurred " + e)
    except SupermarketError as s:
        print(s)

def list_products():
    available_products = supermarket_service.get_all_available_products()

    for available_product in available_products:
        print(f"""
                Product Id - {available_product.product_id}
                Product Name - {available_product.name}
                Price - {available_product.price}
                Available Quantity - {available_product.quantity}""")

    time.sleep(1)

def create_order():
    try:
        print("Available Customers")

        for customer in supermarket_service.get_all_customers():
            print(customer)
        order_id = input("Enter Order Id: ")
        customer_id = input("Enter customer id: ")

        created_order = supermarket_service.add_order(order_id, customer_id)
        print(f"Order {order_id} Created Successfully")
        print(created_order)
    
        time.sleep(1)

    except ValueError as e:
        print(e)
    except SupermarketError as s:
        print(s)

def add_items_to_order():
    order_id = input("Enter Order Id: ")
    product_id = input("Enter Product id: ")
    quantity = int(input("Enter Quantity: "))

    added_items = supermarket_service.add_item_to_order(order_id, product_id, quantity)
    print(f"Order {order_id} Added Successfully")
    print(added_items)

    time.sleep(1)

while True:
    print("""
            1. Add product
            2. Add Customer
            3. List Product
            4. Create Order
            5. Add item to order """)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_product()

    if choice == 2:
        add_customer()

    if choice == 3:
        list_products()

    if choice == 4:
        create_order()

    if choice == 5:
        add_items_to_order()