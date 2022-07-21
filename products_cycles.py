import requests
import json




products = requests.get('http://18.197.23.213/products/')
products_data = json.loads(products.text)
# print(products_data)


