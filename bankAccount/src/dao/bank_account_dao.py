from src.utils.db import db_conn

# Gets account balance
def get_account_balance(bank_id):
    try:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute("select bank_account_balance from bank_account where (bank_account_id = %s)", (bank_id,))
        balance_row = cur.fetchall()
        return balance_row
    finally:
        conn.close()

# Deduct from account balance
def deduct_account_balance(bank_id, new_amount):
    try:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute("update bank_account set bank_account_balance = %s where bank_account_id = %s", (new_amount, bank_id))
        conn.commit()
    finally:
        conn.close()