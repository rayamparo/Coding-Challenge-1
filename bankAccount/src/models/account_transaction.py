class AccountTransaction:

    def __init__(self, account_transaction_owner, account_transaction_id, account_transaction_type, account_transaction_vendor, account_transaction_amount):
        self._account_transaction_owner = account_transaction_owner
        self._account_transaction_id = account_transaction_id
        self._account_transaction_type = account_transaction_type
        self._account_transaction_vendor = account_transaction_vendor
        self._account_transaction_amount = account_transaction_amount