
sleep_hours = []

for i in range(7):

    sleep_input = int(input("Enter no of hours you slept per day: "))

    sleep_hours.append(sleep_input)

average_sleep = sum(sleep_hours) / len(sleep_hours)

print(f"Your average sleep hrs: {average_sleep}")

over_8_hrs_sleep = [hours for hours in sleep_hours if hours > 8]
print(over_8_hrs_sleep)