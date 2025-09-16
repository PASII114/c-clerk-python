from dataclasses import dataclass

from typing import List

from supermarket.models import SupermarketError
from models import Product, Customer, OrderItem, Order

from repositories import ProductRepository, CustomerRepository, OrderRepository


@dataclass
class SupermarketService:

    products: ProductRepository  #using abstract classes as our types
    customer: CustomerRepository
    order: OrderRepository


    def add_products(self, product_id: str, name: str, price: float, quantity: int) -> Product:
        if self.products.get_by_id(product_id) is not None:
            raise SupermarketError(f"Product already exists with product id - {product_id}")
        if quantity < 0:
            raise SupermarketError("Quantity cannot be less than zero")
        if price < 0:
            raise SupermarketError("PRice cannot be less than zero")
        product = Product(product_id, name, price, quantity)
        self.products.add(product)
        return product

    def list_all_products(self):
        return self.products.list_all_products()

    def add_quantity(self, product_id, quantity):
        if self.products.get_by_id(product_id) is None:
            raise SupermarketError(f"Product is not available with product id: {product_id}")

        quantity = Product.add_quantity(product_id, quantity)
        return quantity

    def remove_quantity(self, product_id, quantity):
        if self.products.get_by_id(product_id) is None:
            raise SupermarketError(f"Product is not available with product id: {product_id}")

        Product.reduce_quantity(product_id, quantity)

    def add_customer(self, customer_id: str, name: str, email: str, phone: str) -> Customer:
        if self.customer.get_by_id(customer_id) is not None:
            raise SupermarketError(f"Customer already exists with customer id - {customer_id}")

        customer = Customer(customer_id, name, email, phone)
        self.customer.add(customer)
        return customer

    def add_order(self, order_id: str, customer_id: str) -> Order:

        if self.order.get_by_id(order_id) is not None:
            raise SupermarketError("Order already exist")

        customer = self.customer.get_by_id(customer_id)

        if customer is None:
            raise SupermarketError("Customer doesn't exist")

        order = Order(order_id, customer_id, customer.name)
        self.order.add(order)

        return order

    def get_all_available_products(self) -> List[Product]:
        return [product for product in self.products.list_all_products() if product.is_available()]

    def get_products(self) -> list:
        return self.products.list_all_products()

    def add_item_to_order(self, order_id: str, product_id: str, quantity: int) -> OrderItem:

        order = self.order.get_by_id(order_id)
        products = self.products.get_by_id(product_id)

        if order is None:
            raise SupermarketError("Order doesn't exist")
        if products is None:
            raise SupermarketError("Product doesn't exist")

        if products.quantity < quantity:
            raise SupermarketError(f"Not enough {products.name}s left")

        order_item = OrderItem(product_id, products.name, quantity, products.price)

        order.add_order(order_item)
        products.reduce_quantity(quantity)
        self.products.update(products)
        self.order.update(order)

        return order_item

    def get_all_customers(self) -> List[Customer]:
        return self.customer.list_all_customers()