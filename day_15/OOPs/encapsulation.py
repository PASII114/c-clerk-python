

class BankAccount:

    def __init__(self, owner: str, account_balance: float):
        self.__owner = owner
        self.__account_balance = account_balance

    def get_owner_info(self):
        return self.__owner

    def get_account_balance(self):
        return self.__account_balance