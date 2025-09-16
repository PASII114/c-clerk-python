#one box can contain 12 eggs, when user inputs no of eggs calculate how many boxes
# the boxes  should be filled print remaining amount as well.

eggs_amount = int(input("Enter Eggs Amount"))

box = eggs_amount//12
remaining_eggs = eggs_amount%12

print( box,f"Egg Boxes & Remaining" ,remaining_eggs, "Eggs" )

