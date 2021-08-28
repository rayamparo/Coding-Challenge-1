from src.app import app
from flask import request, Response
from json import dumps
import src.service.transaction_service as transaction_service
from src.models.bank_account import ClassEncoder
from src.models.account_transaction import AccountEncoder

@app.route('/account/<int:bank_id>/deposit', methods=['GET', 'POST'])
def deposit_and_history(bank_id):
    if request.method == 'GET':
        deposits = transaction_service.get_past_deposits(bank_id)
        return dumps(deposits, cls=ClassEncoder)
    if request.method == 'POST':
        req_body = request.get_json()
        deposit = transaction_service.post_new_deposit(bank_id, req_body)
        if deposit == 'Please try to deposit again':
            return Response('Error: Please try to deposit again', status=404)
        else:
            return Response(f'Successfully deposited {req_body["account_transaction_amount"]} into your account')