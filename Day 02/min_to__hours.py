# when user inputs no of minutes, we should output the no of hours and remaining minutes

total_minutes = int(input("Enter Total Minutes"))

hours = total_minutes//60
remaining_mins = total_minutes%60

print( hours,f"Hours & " ,remaining_mins, "mins" )
