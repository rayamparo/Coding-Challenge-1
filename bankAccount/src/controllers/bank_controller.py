from src.app import app
from src.models.bank_account import ClassEncoder
import src.service.bank_account_service as bank_service
from flask import Response
from json import dumps

@app.route('/account/<int:bank_id>', methods=['GET'])
def get_account_balance(bank_id):
    balance_amount = bank_service.get_account_balance(bank_id, 'current')
    json_balance = dumps(balance_amount, cls=ClassEncoder)
    return Response(json_balance, status=200)