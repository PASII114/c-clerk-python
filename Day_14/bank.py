from Day_14.sampath.savings import SavingsAccount
from Day_14.sampath.user import User
from Day_14.sampath.current import CurrentAccount
from Day_14.sampath.account import Account

users = []
accounts = []

def find_user(nic_no):
    for user in users:
        if user.get_nic() == nic_no:
            return user

    return None

def list_users():
    for user in users:
        print(f""" UserName - {user.get_name()}
User nic - {user.get_nic()}""")

def list_accounts():
    for account in accounts:
        print(f"""Account no - {account.get_account_no()}
Balance    - {account.get_balance()}""")


def find_account(account_no):
    for account in accounts:
        if account.get_account_no() == account_no:
            return account

    return None

def get_cheque_ids():

    ids = []

    for account in accounts:
        if isinstance(account, CurrentAccount):
            ids.extend(account.get_cheques())

    for cheque in ids:
        print(cheque)

while True:

    print(
        """
        1. Press 1 to create an user
        2. Press 2 to create an Account
        3. Press 3 to create a Current Account
        4. Press 4 to List All Users
        5. Press 5 to List All Accounts
        6. Press 6 to Deposit
        7. Press 7 to Withdraw
        8. Press 8 to list all Cheque Ids
        """)

    choice = int(input("Enter User Choice: "))

    if choice == 1:
         name = input("Enter name: ")
         nic = int(input("Enter NIC number: "))
         mobile = input("Enter mobile number: ")
         email = input("Enter email: ")
         address = input("Enter address: ")

         user_obj = User(name, nic, mobile, email, address)

         users.append(user_obj)

    if choice == 2:

        account_no = input("Enter Account no: ")
        balance = float(input("Enter Balance: "))
        branch = input("Enter Branch: ")
        atm_card_no = input("Enter Card NO: ")
        nic = int(input("Enter NIC No: "))

        user = find_user(nic)

        if user:
            account_obj = SavingsAccount(account_no, balance, branch, user, atm_card_no)

            accounts.append(account_obj)


    if choice == 3:

        account_no = input("Enter Account no: ")
        balance = float(input("Enter balance: "))
        branch = input("Enter branch: ")
        cheque_id = input("Enter cheque id: ")
        nic = int(input("Enter NIC no: "))

        user = find_user(nic)

        if user:
            account_obj = CurrentAccount(account_no, balance, branch, user, [cheque_id])

            accounts.append(account_obj)


    if choice == 4:
        list_users()

    if choice == 5:
        list_accounts()

    if choice == 6:
        account_no = input("Enter account no: ")

        account = find_account(account_no)
        print(isinstance(account, SavingsAccount))

        if account:
            deposit_amount = float("Enter deposit amount: ")
            account.deposit(deposit_amount)

    if choice == 7:
        account_no = input("Enter account no: ")

        account = find_account(account_no)

        if account:
            withdrawal_amount = float("Enter withdraw amount: ")
            account.withdrawal(withdrawal_amount)

            print(f"Rs. {withdrawal_amount} amount withdrew successfully.")


    if choice == 8:
        get_cheque_ids()