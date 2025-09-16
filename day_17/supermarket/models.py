from dataclasses import dataclass, field
from datetime import datetime
from typing import List

class SupermarketError(Exception):
    pass

@dataclass
class Product:
    product_id:str
    name:str
    price:float
    quantity:int

    def is_available(self) -> bool:
        return self.quantity > 0

    def add_quantity(self, quantity: int):
        if quantity < 0:
            raise SupermarketError("Quantity cannot be less than 0")
        self.quantity += quantity

    def reduce_quantity(self, quantity: int) ->None:
        if quantity > self.quantity:
            raise SupermarketError("Quantity is not enough")
        else:
            self.quantity -= quantity



@dataclass
class Customer:
    customer_id:str
    name:str
    email:str
    phone:str

@dataclass
class OrderItem:
    product_id:str
    product_name:str
    quantity:int
    unit_price:float

    def total_price(self) -> float:
        price = self.quantity * self.unit_price
        return price

@dataclass
class Order:
    order_id:str
    customer_id:str
    customer_name:str
    order_time: datetime = field(default_factory=datetime.now)
    items: List[OrderItem] = field(default_factory=list) #create a brand-new object for each instance created in OrderItem

    def add_order(self, order: OrderItem) -> None:
        self.items.append(order)

    def total_amount(self) -> float:
        return sum(item.total_price() for item in self.items)

    def item_count(self) -> int:
        return len(self.items)

if __name__ == '__main__':
    order1 = Order("111", "111", "Anura", datetime.now())
    print(order1)

    order_item = OrderItem("001", "Apples", 20, 200.00)

    order1.items.append(order_item)

    print(order1.order_time)
    print(order_item.total_price())