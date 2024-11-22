import requests

PRODUCT_SERVICE_URL = 'http://127.0.0.1:5001'

def check_availability(product_ids, quantities):
    response = requests.post(f"{PRODUCT_SERVICE_URL}/check-availability", json={
        "product_ids": product_ids,
        "quantities": quantities
    })
    return response.json().get('available')

def get_total_price(product_ids, quantities):
    response = requests.post(f"{PRODUCT_SERVICE_URL}/calculate-price", json={
        "product_ids": product_ids,
        "quantities": quantities
    })
    return response.json().get('total_price')

def update_inventory(product_ids, quantities):
    requests.post(f"{PRODUCT_SERVICE_URL}/update-inventory", json={
        "product_ids": product_ids,
        "quantities": quantities
    })