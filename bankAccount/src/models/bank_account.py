from json import JSONEncoder
from src.models.account_transaction import AccountTransaction

class BankAccount:

    def __init__(self, bank_account_id=None, bank_account_balance=None, bank_transactions_list=None):
        self._bank_account_id = bank_account_id
        self._bank_account_balance = bank_account_balance
        self._bank_transactions_list = bank_transactions_list

class ClassEncoder(JSONEncoder):
    def default(self, class_obj):
        if isinstance(class_obj, BankAccount):
            return class_obj.__dict__
        elif isinstance(class_obj, AccountTransaction):
            return class_obj.__dict__
        else:
            return super().default(self, class_obj)