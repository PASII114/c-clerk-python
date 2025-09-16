#should have list of available products with price
#implement method to view available products and implement the function to find a product by id

available_products = [
    {"id" : 1, "product" : "Orange Juice", "price": 150},
    {"id" : 2, "product" : "Grape Juice", "price" : 100},
    {"id": 3, "product": "Apple Juice", "price": 120},
    {"id": 4, "product": "Wood Apple Juice", "price": 150},
    {"id": 5, "product": "Mixed Juice", "price": 200}
]

def view_products():
    for products in available_products:
        print(f"{products["id"]}. {products["product"]} : Rs.{products["price"]}")

def search_product_by_id(products, product_id):

    for product in products:
        if product_id == product["id"]:
            return product

    return  None

if __name__ == "__main__":
    search_product_by_id(available_products, 1)
