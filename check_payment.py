import hashlib
import requests

secret_key = '7lWI4rX8pbS8UyEw'

url = 'https://d0ef-213-230-121-237.ngrok.io/success/'

data = {
    'pg_order_id': '23',
    'pg_payment_id': '677919083',
    'pg_amount': '25',
    'pg_salt': '5ZlHodSBc8MrhYBN',
    'pg_currency': 'KZT'
}

string = ''
for i in sorted(data.keys()):
    string = string + str(data[i]) + ';'

q = f'init_payment.php;{string}{secret_key}'
sig = (hashlib.md5(f'init_payment.php;{string}{secret_key}'.encode()).hexdigest())
data['pg_sig'] = sig
res = requests.post(url=url, data=data)
print(res.text)
