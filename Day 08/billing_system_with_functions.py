#Billing System
# take input price, quantity, is member
#when user enter price and quantity, we should calculate total price
#write a function to print the final bill with customer name
#we should write a function to give a discount if he's a member an if the bill is >= 5000

print("""Billing System""")

def total_price(price, quantity):
    return price * quantity



def final_amount(bill_total, membership_status):
    if membership_status and bill_total >= 5000:
        return bill_total * 0.8

    else:
        return bill_total

product_price = float(input("Enter the price of the item: "))
product_quantity = int(input("Enter the quantity: "))
user_is_member = input("Is the customer a member (yes/no): ") == "yes"


total = total_price(product_price, product_quantity)

user_final_amount = final_amount(total, user_is_member)

print(f"Customer Final Amount is: {user_final_amount}")