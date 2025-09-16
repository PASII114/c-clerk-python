# from Day_14.bank import user_obj


class Account:

    def __init__(self, account_no, balance, branch, user): #user - composition
        self.__account_no = account_no
        self.__balance = balance
        self.__branch = branch
        self.__user = user

    def deposit(self, deposit_amount):
        self.__balance = self.__balance + deposit_amount

    def withdrawal(self, withdrawal_amount):
        self.__balance = self.__balance - withdrawal_amount

    def set_account_no(self, account_no): #encapsulation
        self.__account_no = account_no

    def get_account_no(self):
        return self.__account_no

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def check_balance(self):
        print(f"Your account balance is - {self.__balance}")

    def set_branch(self, branch):
        self.__branch = branch

    def get_branch(self):
        return self.__branch

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user