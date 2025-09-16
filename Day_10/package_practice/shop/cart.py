cart_items = []

def add_to_cart(product, quantity):
    cart_items.append({"product" : product, "quantity" : quantity})
    print(f"{product['product']} * {quantity} Added to cart successfully")


def remove_from_cart(product_id):
    global cart_items
    # cart = []
    #
    # for item in cart_items:
    #     if item["product"]["id"] != product_id:
    #         cart.append(item)
    # cart_items = cart[:]

    cart_items = [item for item in cart_items if item["product"]["id"] != product_id]
    print(f"Removed product - {product_id}")

def view_cart():
    for item in cart_items:
        print(f"{item['product']} : {item['quantity']}")