import src.dao.transaction_dao as transaction_dao
from datetime import date
from src.models.account_transaction import AccountTransaction

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