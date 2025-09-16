from Day_10.package_practice.shop.billing import shop_checkout
from shop import billing, products, cart

def main():
    print("""===========================MENU===========================
    1. View Products
    2. Search Product
    3. Add Product to Cart
    4. View Cart
    5. Remove Items from Cart
    6.Checkout""")

    choice = int(input("Enter Your Choice (1-5): "))

    if choice == 1:
        products.view_products()

    if choice == 2:
        product_id = int(input("Enter product id: "))

        products.search_product_by_id(products.available_products, product_id)

    if choice == 3:
        products.view_products()
        product_id = int(input("Enter the product: "))

        if products.search_product_by_id(products.available_products, product_id) is None:
            print("Sorry this Product is not available")
        else:
            quantity = int(input("Enter the quantity: "))

            cart.add_to_cart(products.search_product_by_id(products.available_products, product_id), quantity)

    if choice == 4:
        cart.view_cart()

    if choice == 5:
        cart.view_cart()
        product_id = int(input("Enter the product id you want to remove: "))

        cart.remove_from_cart(product_id)

    if choice == 6:
        cart.view_cart()
        print(f"{cart.cart_items}")
        if cart.cart_items:

            confirm = int(input("Press 1 to confirm the product list: ")) == 1

            if confirm:
                billing.shop_checkout(cart.cart_items)
        else:
            print("You have no items in your cart")



while True:
    main()