from src.utils.db import db_conn

# Gets account balance
def get_account_balance(bank_id):
    try:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute(f'select bank_account_balance from bank_account where (bank_account_id = %s)', (bank_id,))
        balance_row = cur.fetchall()
        return balance_row
    finally:
        conn.close()