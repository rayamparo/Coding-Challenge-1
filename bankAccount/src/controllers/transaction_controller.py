from src.app import app
from flask import request, Response
from json import dumps
import src.service.transaction_service as transaction_service
from src.models.bank_account import ClassEncoder

# Gets and posts deposits
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
            return Response(f'Successfully deposited {req_body["account_transaction_amount"]} into your account', status=200)

# Gets and posts charges
@app.route('/account/<int:bank_id>/charge', methods=['GET', 'POST'])
def charge_and_history(bank_id):
    if request.method == 'GET':
        charges_list = transaction_service.get_past_charges(bank_id)
        return dumps(charges_list, cls=ClassEncoder)
    if request.method == 'POST':
        req_body = request.get_json()
        charge = transaction_service.post_new_charge(bank_id, req_body)
        if charge == 'Successful Transaction':
            return Response('Successful Transaction', status=200)
        elif charge == 'Transaction Rejected: Not enough funds':
            return Response('Transaction Rejected: Not enough funds', status=202)
        return Response('Unsuccessful Transaction: Please try again', status=400)