import time

print("""==========================================
WELCOME TO GEDARA YANA GAMAN SHOPPING MENU
==========================================""")

available_products = ["APPLE", "BANANA", "ORANGE", "MILK", "BREAD"]
cart = []

while True:
    print("""============ Menu ============
1. View Available Products
2. View Cart
3. Checkout
4. Clear Your Cart
5. Exit""")
    menu_choice = int(input("Enter Your Choice (1 - 4): "))
    time.sleep(0.5)

    if menu_choice < 1 or menu_choice > 5:
        print("Please enter a valid choice: ")
        time.sleep(0.5)
        continue

    elif menu_choice == 1:
        while True:
            print("""========== AVAILABLE PRODUCTS ==========""")

            i = 0
            while i < len(available_products):
                print(f"{i + 1}. {available_products[i]}")
                i += 1
                continue

            print("""======================
| 1. Add items to cart  |
| 2. Go back main menu  |
======================""")

            choice = int(input("Please choose your option (1 or 2): "))

            if choice == 2:
                print("Redirecting to main menu....")
                time.sleep(1)
                break

            elif choice == 1:
                add_to_cart_choice = int(input("Please enter which product you want to add to the cart (1 - 4): "))


                if add_to_cart_choice == 1:
                    cart.append(available_products[0])
                    print(f"{available_products[0]} added to cart successfully.")
                    time.sleep(0.5)

                elif add_to_cart_choice == 2:
                    cart.append(available_products[1])
                    print(print(f"{available_products[1]} added to cart successfully."))
                    time.sleep(0.5)

                elif add_to_cart_choice == 3:
                    cart.append(available_products[2])
                    print(print(f"{available_products[2]} added to cart successfully."))
                    time.sleep(0.5)

                elif add_to_cart_choice == 4:
                    cart.append(available_products[3])
                    print(print(f"{available_products[3]} added to cart successfully."))
                    time.sleep(0.5)

                elif add_to_cart_choice == 5:
                    cart.append(available_products[4])
                    print(print(f"{available_products[4]} added to cart successfully."))
                    time.sleep(0.5)

                else:
                    print("Please enter a valid choice.")
                    time.sleep(0.5)

            else:
                print("Please enter a valid choice.")

    elif menu_choice == 2:
        while True:
            if len(cart) == 0:
                print("Your Cart is empty. Redirecting back to main menu....")
                time.sleep(1)
                break

            print("""========== YOUR CART ==========""")

            for item in cart:
                print(f"{item}")
                continue

            remove_item = input("Do you want to remove items from the cart (yes/no)? ").upper() == "YES"
            time.sleep(0.5)

            while remove_item:

                item_to_remove = input("Please select the item you want to remove: ").upper()

                if item_to_remove in available_products:
                    cart.remove(item_to_remove)
                    print(f"{item_to_remove} removed from cart.")
                    break

                # elif item_to_remove == "BANANA":
                #     cart.remove("BANANA")
                #     break
                #
                # elif item_to_remove == "ORANGE":
                #     cart.remove("ORANGE")
                #     break
                #
                # elif item_to_remove == "MILK":
                #     cart.remove("MILK")
                #     break
                #
                # elif item_to_remove == "BREAD":
                #     cart.remove("BREAD")
                #     break
                #
                # while not item_to_remove:
                #     break

            else:
                print("Redirecting to main menu....")
                time.sleep(1)
                break

    elif menu_choice == 3:

        while True:
            if len(cart) == 0:
                print("You have no items in your cart.")
                time.sleep(1)
                break

            print("========== ORDER CONFIRMATION ==========")

            for item in cart:
                print(f"{item}")
                continue

            print("""=======================
| 1. Confirm Order  |
| 2. Buy More Items |
=======================""")


            checkout_choice = int(input("Please choose your option (1-2): "))
            time.sleep(1)

            if checkout_choice == 1:
                are_you_sure = input("Are you sure? (yes/no): ").upper() == "YES"
                time.sleep(1)

                if are_you_sure:
                    cart = []
                    print("Finalizing your order....")
                    time.sleep(1)
                    print("""Your order has been confirmed. Please collect your items from the counter.
====================
THANK YOU FOR COMING
====================""")
                    exit()

                elif not are_you_sure:
                    exit()

            elif checkout_choice == 2:
                print("Going back to main menu....")
                time.sleep(1)
                break

    elif menu_choice == 4:
        if len(cart) <= 0:
            print("You have no items in your cart. Add items to cart before clearing it")
            time.sleep(1)

        else:
            clear_cart_choice = input("Are you sure you want to clear the cart? (yes/no) ").upper() == "YES"

            if clear_cart_choice:
                cart = []
                print("Your cart has been cleared")
                time.sleep(0.5)

            if not clear_cart_choice:
                break

    elif menu_choice == 5:
        print("""================================================
THANK YOU FOR VISITING PAIN YANA GAMAN FOOD MART
================================================""")
        exit()
