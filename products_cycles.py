import requests
import json




products = requests.get('http://18.197.23.213/products/')
products_data = json.loads(products.text)
# print(products_data)

data = {}
for items_prod in products_data['results']:
    for item in items_prod:
        ...
