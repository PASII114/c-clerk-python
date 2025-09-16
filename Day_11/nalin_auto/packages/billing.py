TAX_RATE = 0.2
VAT_RATE = 0.5
SHIPPING_COST = 100000.000


def billing_method():
    print("Printing from billing...")


def calculate_bill(inventory, tax_rate=TAX_RATE, vat_rate=VAT_RATE, shipping=SHIPPING_COST):
    subtotal = 0
    for item in inventory:

        subtotal += item["price"]

    tax = subtotal * tax_rate
    vat = (subtotal + tax) * vat_rate
    grand_total = subtotal + tax + vat + shipping

    return {
        "Subtotal": subtotal,
        "Tax": tax,
        "VAT": vat,
        "Shipping": shipping,
        "Grand Total": grand_total
    }



