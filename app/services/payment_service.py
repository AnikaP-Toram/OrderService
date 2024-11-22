import requests

PAYMENT_SERVICE_URL = 'http://127.0.0.1:5002'

def process_payment(transaction_id, total_price, order_id, user_id):
    requests.post(f"{PAYMENT_SERVICE_URL}/create-transaction", json={
        "transaction_id": transaction_id,
        "total_price": total_price,
        "order_id": order_id,
        "user_id": user_id
    })
