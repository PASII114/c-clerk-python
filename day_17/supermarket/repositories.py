from abc import ABC, abstractmethod
from typing import List, Dict

from models import Product
from models import Customer
from models import Order

class ProductRepository(ABC):

    @abstractmethod
    def add(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_by_id(self, product_id: str) -> Product:
        pass

    @abstractmethod
    def list_all_products(self) -> List[Product]:
        pass

    @abstractmethod
    def update(self, product: Product) -> None:
        pass


class CustomerRepository(ABC):

    @abstractmethod
    def add(self, customer: Customer):
        pass

    @abstractmethod
    def get_by_id(self, customer_id: str) -> Customer:
        pass

    @abstractmethod
    def list_all_customers(self) -> List[Customer]:
        pass


class OrderRepository(ABC):

    @abstractmethod
    def add(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def list_all_orders(self) -> List[Order]:
        pass

    @abstractmethod
    def update(self, order: Order) -> None:
        pass


class InMemoryProductRepository(ProductRepository):

    def __init__(self):
        self.__product: Dict[str, Product] = {}

    def add(self, product: Product) -> None:
        self.__product[product.product_id] = product

    def get_by_id(self, product_id: str) -> Product:
        return self.__product.get(product_id)

    def list_all_products(self) -> List[Product]:
        return list(self.__product.values())

    def update(self, product: Product) -> None:
        self.__product[product.product_id] = product


class InMemoryCustomerRepository(CustomerRepository):

    def __init__(self):
        self.__customer: Dict[str, Customer] = {}

    def add(self, customer: Customer):
        self.__customer[customer.customer_id] = customer

    def get_by_id(self, customer_id: str) -> Customer:
        return self.__customer.get(customer_id)

    def list_all_customers(self) -> List[Customer]:
        return list(self.__customer.values())

    def update(self, customer: Customer):
        self.__customer[customer.customer_id] = customer

class InMemoryOrderRepository(OrderRepository):

    def __init__(self):
        self.__order: Dict[str, Order] = {}

    def add(self, order: Order) -> None:
        self.__order[order.order_id] = order

    def get_by_id(self, order_id: str) -> Order:
        return self.__order.get(order_id)

    def list_all_orders(self) -> List[Order]:
        return list(self.__order.values())

    def update(self, order: Order) -> None:
        self.__order[order.order_id] = order