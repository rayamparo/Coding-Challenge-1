from src.app import app
from flask import request, Response
from json import dumps

@app.route('/account/<int:bank_id>/deposit', methods=['GET', 'POST'])
def deposit_and_history(bank_id):
    if request.method == 'GET':
        pass