monthly_salary = float(input("Enter your monthly salary: Rs."))
#annual_salary = float(input("Enter your annual salary: "))
annual_salary = monthly_salary * 12
total_tax = 0

if annual_salary <= 1200000:
    print("You are tax free!!")
else:
    taxable_amount = annual_salary - 1200000

    if taxable_amount <= 500000:
        total_tax = taxable_amount * 0.06
        print(f"Your annual tax amount is: Rs.{total_tax}")
        print(f"Your monthly tax amount is: Rs.{total_tax/12}")
    elif taxable_amount <= 1000000:
        total_tax = (((taxable_amount - 500000) * 0.12) + (500000 * 0.06))
        print(f"Your annual tax amount is: Rs.{total_tax}")
        print(f"Your monthly tax amount is: Rs.{total_tax / 12}")
    elif taxable_amount <=1500000:
        total_tax = (500000 * 0.06) + (500000 * 0.12) + ((taxable_amount - 1000000) * 0.18)
        print(f"Your annual tax amount is: Rs.{total_tax}")
        print(f"Your monthly tax amount is: Rs.{total_tax / 12}")
    elif taxable_amount <= 2000000:
        total_tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + ((taxable_amount - 1500000) * (24/100))
        print(f"Your annual tax amount is: Rs.{total_tax}")
        print(f"Your monthly tax amount is: Rs.{total_tax / 12}")
    elif taxable_amount <= 2500000:
        total_tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * (24 / 100)) + ((taxable_amount - 2500000) * (30/100))
        print(f"Your annual tax amount is: Rs.{total_tax}")
        print(f"Your monthly tax amount is: Rs.{total_tax / 12}")
    else:
        print("$$$$$$ Your income is THROUGH THE ROOFS $$$$$$.")


print(f"Your take home salary is: Rs.{monthly_salary - total_tax / 12}")