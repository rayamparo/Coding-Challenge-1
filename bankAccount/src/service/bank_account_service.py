import src.dao.bank_account_dao as bank_dao
from src.models.bank_account import BankAccount

# Gets account balance
def get_account_balance(bank_id, msg):
    account_balance = bank_dao.get_account_balance(bank_id)
    balance_amount = account_balance[0][0]
    current_amount = BankAccount(bank_account_balance=balance_amount)
    if msg == 'current':
        return current_amount
    elif msg == 'balance':
        return balance_amount

# Deducts from account balance
def deduct_account_balance(bank_id, transaction_amount):
    current_amount = get_account_balance(bank_id, 'balance')
    remove_dollar = current_amount.replace('$', '')
    float_current = float(remove_dollar.replace(',', ''))
    if float_current - transaction_amount < 0.0:
        return 'Transaction Rejected: Not enough funds'
    new_amount = float_current - transaction_amount
    bank_dao.deduct_account_balance(bank_id, new_amount)
    return 'Successful Transaction'