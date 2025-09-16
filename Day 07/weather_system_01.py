#weather tracking system
#for each hour everyday we track the temperature we do this for 31 days
#have menu with 4 options
#1st - add a temperature - ask user which day as input (1-7)
#ask user which hour as input (1-3)
import time

print("Weather Tracking System")

# temps_per_day_for_week = [[0.0 for i in range(3)] for i in range(7)]
#
# for temps_per_days in temps_per_day_for_week:
#     print(temps_per_days)

print("""==========Menu==========""")
print("""1. Add a Temperature
2. Look at Temperature of a Day
3. Average Temperature of a Day
4. Highest Temperature of a Day
5. Hottest Hour of a Day
6. Average Temperature for the Whole Week""")



temps_per_day_for_week = [ [0.0 for _ in range(3)] for _ in range(7) ]

while True:
    choice = int(input("Enter Your Choice (1 - 2): "))

    if choice == 1:
        day = int(input("Enter a day from (1 - 7): ")) - 1
        hour = int(input("Enter an hour from (1 - 3): ")) - 1
        temp = float(input("Enter temperature in celcious: "))

        temps_per_day_for_week[day][hour] = temp

        for temperatures in temps_per_day_for_week:
            print(temperatures)

        time.sleep(2)

    if choice == 2:
        day = int(input("Enter a day from (1 - 7): ")) - 1
        hour = int(input("Enter an hour from (1 - 3): ")) - 1

        get_temperature = temps_per_day_for_week[day][hour]

        print(f"Temperature of day {day + 1} is: {get_temperature}°C")

    if choice == 3:
        day = int(input("Enter a day from (1 - 7): ")) - 1

        avg_temp = sum(temps_per_day_for_week[day]) / 3

        print(f"Average Temperature of {day + 1} is: {avg_temp}℃")

    if choice == 4:
        day = int(input("Enter a day from (1 - 7): ")) - 1

        highest_temp = max(temps_per_day_for_week[day])

        print(f"Highest Temperature of {day + 1} is: {highest_temp}℃")

    if choice == 5:
        day = int(input("Enter a day from (1 - 7): ")) - 1

        hottest_hour = temps_per_day_for_week.index(max([temps_per_day_for_week][day]))

        print(f"Hottest Hour of {day + 1} is: {hottest_hour + 1}")

    if choice == 6:

        total = 0

        for i in temps_per_day_for_week:
            for j in i:
                total += j
        print(f"Average Temperature of the Month is: {total / 21}")