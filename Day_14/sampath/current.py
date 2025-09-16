from Day_14.sampath.account import Account


class CurrentAccount(Account):

    def __init__(self, account_no, balance, branch, user, cheque_ids):
        Account.__init__(self, account_no, balance, branch, user)
        self.__cheque_ids = cheque_ids

    def get_cheques(self):
        return self.__cheque_ids

    def set_cheque_ids(self, cheque_ids):
        self.__cheque_ids = cheque_ids

    def add_cheque_id(self, cheque_id):
        self.__cheque_ids.append(cheque_id)