from src.app import app
from src.models.bank_account import ClassEncoder
import src.service.bank_account_service as bank_service
from flask import Response
from json import dumps

@app.route('/account/<int:bank_id>', methods=['GET'])
def get_account_balance(bank_id):
    balance_amount = bank_service.get_account_balance(bank_id)
    print_this = dumps(balance_amount, cls=ClassEncoder)
    print(print_this)
    return 'Working'