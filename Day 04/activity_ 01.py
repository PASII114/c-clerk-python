#simple ATM

#pin = 0000
#amount = 5000

#user enters the pin
    #-has to validate whether the pin is correct and proceed
#if pin is correct show the menu
    #1. check balance
    #2. deposit money
    #3. withdraw money - check available balance when withdrawing, if balance is less, restrict
    #4. exit

#user should be able to perform these activities until he decides to exit the program

import time

print("💲💲💲 WELCOME TO THE ATM 💲💲💲")
print("Please enter your bank card HERE:")
pin = "0000"
available_amount = 5000
attempts = 0

while True:
            usr_pin = input("Enter your PIN number: ")

            if usr_pin != pin:
                attempts += 1
                print("Checking whether the pin is correct......")
                print("❌ Invalid PIN number ❌ Only 2 attempts left")

                if attempts == 3:
                    print("Maximum Attempts Reached. Exiting The Program")
                    exit()

            else:
                print("Your PIN number is correct. Proceeding to the Menu")
                time.sleep(2)
                while True:
                    print("""
                    --------MENU---------    
                    1. Check Your Balance
                    2. Deposit Money
                    3. Withdraw Money
                    4. Exit""")

                    action = int(input("Choose the action you want to perform: "))

                    if action == 1:
                        print(f"Your available amount is: Rs.{available_amount}")
                        time.sleep(4)
                    elif action == 2:
                        deposit_amount = float(input("Enter the amount you want to deposit: Rs."))

                        if deposit_amount <= 0:
                            print("Please enter a valid amount to deposit")
                            time.sleep(3)
                        else:
                            available_amount = available_amount + deposit_amount
                            print("Amount deposited successfully.")
                            print(f"Account Balance: Rs.{available_amount}")
                            time.sleep(3)
                    elif action == 3:
                        withdraw_amount = float(input("Please enter the amount you want to withdraw: Rs."))
                        if withdraw_amount > available_amount:
                            print("You don't have enough balance to withdraw. Please enter a valid amount.")
                            time.sleep(5)
                        elif withdraw_amount <= 0:
                            print("Please enter a valid amount to withdraw")
                            time.sleep(3)
                        else:
                            print(f"Withdrawing Rs.{withdraw_amount}")
                            available_amount = available_amount - withdraw_amount
                            print(f"{withdraw_amount} amount withdrawal successfully")
                            print(f"Account Balance: {available_amount}")
                            time.sleep(6)
                    elif action == 4:
                        print("Exiting the ATM")
                        print("Thank You for using the ATM")
                        exit()
                    else:
                        print("Please enter a valid choice")