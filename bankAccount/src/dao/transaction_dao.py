from src.utils.db import db_conn

# Gets all past deposits
def get_past_deposits(bank_id):
    try:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute("select * from account_transaction where (account_transaction_owner = %s and account_transaction_type = 'Deposit')", (bank_id,))
        all_deposits = cur.fetchall()
        return all_deposits
    finally:
        conn.close()

# Posts a new deposit
def post_new_deposit(bank_id, amount, date):
    try:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute("insert into account_transaction values (%s, default, 'Deposit', null, %s, %s)", (bank_id, amount, date))
        conn.commit()
    finally:
        conn.close()

# Post new charge
def post_new_charge(bank_id, vendor, amount, date):
    try:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute("insert into account_transaction values (%s, default, 'Charge', %s, %s, %s)", (bank_id, vendor, amount, date))
        conn.commit()
    finally:
        conn.close()

# Get all past charges
def get_past_charges(bank_id):
    try:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute("select * from account_transaction where (account_transaction_owner = %s and account_transaction_type = 'Charge')", (bank_id,))
        all_charges = cur.fetchall()
        return all_charges
    finally:
        conn.close()