import requests


def verify(phone_number, code):
    URL = "http://notify.eskiz.uz/api/message/sms/send"
    PARAMS = {
        "Authorization": ""}
    phone = str(phone_number)[1:13]
    data = {
        'mobile_phone': phone,
        'message': code,
        'from': "4546",
        'callback_url': 'http://0000.uz/test.php'
    }

    response = requests.request("POST", URL, data=data, headers=PARAMS)
    print(response.json())
    return response