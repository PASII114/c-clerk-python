#if height is lower than 1.2, cannot purchase the ticket
#if the age is less than 20, 20% discount, if age is 60, 50% discount
#ticket price 1000

print("""If you're under 18 year old༼ つ ◕_◕ ༽つ, you get a 20% discount ^_^ and 
if you're over 60 or 60 years old (⊙_⊙;) you get a 50% discount ^_^
but you have to be over 1.2 meters tall(¬‿¬).""")

height = float(input("Enter your height(m): "))
ticket_price = 1000

if height < 1.2:
    print("You cannot purchase a ticket. Sorry＞﹏＜")
else:
    age = int(input("Enter your age(years): "))
    if age < 18:
        final_ticket_price = ticket_price - ((1000 * 20) / 100)
        print(f"Your ticket price is Rs.{final_ticket_price}")
    elif age >= 60:
        final_ticket_price = ticket_price - ((1000 * 50) / 100)
        print(f"Your ticket price is Rs.{final_ticket_price}")
    else:
        print(f"Your ticket price is Rs.{ticket_price}")