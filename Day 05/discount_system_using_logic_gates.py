#bill value > 5000
#is coupons used
##is member
#if not buying vegetables
#if all true discount = 20%

bill_value = float(input("Enter the bill amount: "))
is_buying_vegetables = input("Is customer buying vegetables: yes/no: ") == "yes"
is_using_coupon = input("Is customer using a coupon: yes/no: ") == "yes"
is_member = input("Is customer a member: yes/no: ") == "yes"

discount = "20%"
eligibility = (bill_value > 5000 and
               not is_buying_vegetables and
               not is_using_coupon and
               is_member)

if eligibility:
    print(f"You are eligible for a {discount} discount")
else:
    print("You are not eligible for a discount")