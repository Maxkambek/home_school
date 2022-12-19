import hashlib
import requests

secret_key = '7lWI4rX8pbS8UyEw'

url = 'https://1177-213-230-121-237.ngrok.io/success/'

data = {
    'pg_order_id': '23',
    'pg_merchant_id': '547013',
    'pg_amount': '25',
    'pg_description': 'test',
    'pg_salt': 'molbulak',
    'pg_currency': 'KZT',
    'pg_check_url': 'https://1177-213-230-121-237.ngrok.io/success/',
    'pg_result_url': 'https://1177-213-230-121-237.ngrok.io/success/',
    'pg_request_method': 'POST',
    'pg_success_url': 'https://1177-213-230-121-237.ngrok.io/success/',
    'pg_failure_url': 'https://1177-213-230-121-237.ngrok.io/success/',
    'pg_success_url_method': 'GET',
    'pg_failure_url_method': 'GET'
}

string = ''
for i in sorted(data.keys()):
    string = string + str(data[i]) + ';'

q = f'init_payment.php;{string}{secret_key}'
sig = (hashlib.md5(f'init_payment.php;{string}{secret_key}'.encode()).hexdigest())
data['pg_sig'] = sig
res = requests.post(url=url, data=data)
print(res.text)
