from src.utils.db import db_conn

# Gets all past deposits
def get_past_deposits(bank_id):
    try:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute('select account_transaction_vendor, account_transaction_amount from account_transaction where (account_transaction_owner = %s and account_transaction_type = "Deposit")', (bank_id,))
        all_deposits = cur.fetchall()
        return all_deposits
    finally:
        conn.close()