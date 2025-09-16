SERVICE_CHARGE = 0.1
VAT_RATE = 0.18

def billing_process(cart_items):
    subtotal = 0
    for item in cart_items:
        subtotal += item["product"]["quantity"] * item["product"]["price"]

    # subtotal = sum([item["product"]["quantity"] * item["product"]["price"] for item in cart_items])

    service_charge = SERVICE_CHARGE * subtotal
    vat = VAT_RATE * subtotal

    return subtotal, service_charge, vat

def shop_checkout(cart_items):
    subtotal, service_charge, vat = billing_process(cart_items)

    print(f"Subtotal - {subtotal}")
    print(f"Service Charge - {service_charge}")
    print(f"VAT - {vat}")
    print(f"Total Amount - {subtotal} + {service_charge} + {vat}")