from json import JSONEncoder

class AccountTransaction:

    def __init__(self, account_transaction_owner, account_transaction_id, account_transaction_type, account_transaction_vendor, account_transaction_amount, account_transaction_date):
        self._account_transaction_owner = account_transaction_owner
        self._account_transaction_id = account_transaction_id
        self._account_transaction_type = account_transaction_type
        self._account_transaction_vendor = account_transaction_vendor
        self._account_transaction_amount = account_transaction_amount
        self._account_transaction_date = account_transaction_date

class AccountEncoder(JSONEncoder):
    def default(self, class_obj):
        # if isinstance(class_obj, AccountTransaction):
        #     return class_obj.__dict__
        # else:
        #     return super().default(self, class_obj)
        return class_obj.__dict__