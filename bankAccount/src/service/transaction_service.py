import src.dao.transaction_dao as transaction_dao
from datetime import date
from src.models.account_transaction import AccountTransaction
import src.service.bank_account_service as bank_service

# Gets all past deposits
def get_past_deposits(bank_id):
    deposit_history = transaction_dao.get_past_deposits(bank_id)
    deposits_dict = {}
    count = 0;
    for deposit in deposit_history:
        deposits_dict[deposit[count]] = AccountTransaction(deposit[0], deposit[1], deposit[2], deposit[3], deposit[4], str(deposit[5]))
        count = count + 1
    return deposits_dict

# Post new deposit
def post_new_deposit(bank_id, req_body):
    if req_body['account_transaction_type'] == 'deposit' or req_body['account_transaction_type'] == 'Deposit':
        current_date = date.today()
        transaction_dao.post_new_deposit(bank_id, req_body['account_transaction_amount'], current_date)
        return f'Successfully deposited {req_body["account_transaction_amount"]} into your account'
    return 'Please try to deposit again'


# Gets all past charges
def get_past_charges(bank_id):
    charges_rows = transaction_dao.get_past_charges(bank_id)
    charges_dict = {}
    count = 0;
    for charge in charges_rows:
        charges_dict[charge[count]] = AccountTransaction(charge[0], charge[1], charge[2], charge[3], charge[4], str(charge[5]))
        count = count + 1
    return charges_dict

# Post new charge
def post_new_charge(bank_id, req_body):
    transaction_type = req_body['account_transaction_type']
    transaction_amount = req_body['account_transaction_amount']
    transaction_vendor = req_body['account_transaction_vendor']
    if transaction_type == 'charge' or transaction_type == 'Charge':
        current_date = date.today()
        deduct_from_account = bank_service.deduct_account_balance(bank_id, transaction_amount)
        if deduct_from_account == 'Successful Transaction':
            transaction_dao.post_new_charge(bank_id, transaction_vendor, transaction_amount, current_date)
            return 'Successful Transaction'
        elif deduct_from_account == 'Transaction Rejected: Not enough funds':
            return 'Transaction Rejected: Not enough funds'
    return 'Unsuccessful Transaction: Please try again'
