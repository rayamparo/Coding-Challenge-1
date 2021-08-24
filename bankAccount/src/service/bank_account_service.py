import src.dao.bank_account_dao as bank_dao
from src.models.bank_account import BankAccount

def get_account_balance(bank_id):
    account_balance = bank_dao.get_account_balance(bank_id)
    balance_amount = account_balance[0][0]
    running_amount = BankAccount(bank_account_balance=balance_amount)
    return running_amount