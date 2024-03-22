

import requests
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth


def timestamp():
    unformatted_time=datetime.now()#2024-03-23
    formated_time=unformatted_time.strftime("%Y%m%d%H%M%S")#"20240323"
    print(formated_time)
    return formated_time
    

def password(formated_time):
    #  Shortcode+Passkey+Timestamp bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919
    data_to_encode="174379" + "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919" + formated_time

    encoded_password=base64.b64encode(data_to_encode.encode())

    decoded_password=encoded_password.decode('utf-8')
    print(decoded_password)
    return decoded_password



def generate_access_token():
   
    consumer_key = "pGRYvQYXjJCmkYwhQZABM6HEfzAIvmrbAUqJQsa9zzTcUdkQ"
    consumer_secret = "Gkq1fL4DjAGZGPYUxRHKAUPJUPNuEU3yEK5KGrGRsP2CR8Ne8nU954qExpS6WvEu"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
  
    try:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    except:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret), verify=False)
        
    print(r.text)
    print(r.json())
    json_response = (r.json())  

    my_access_token = json_response["access_token"]
    
    print(my_access_token)
    return my_access_token


def pay_for_rental(request):
    
    formated_time = timestamp()
    access_token=generate_access_token()
    
   
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": "174379",
        "Password": password(formated_time),
        "Timestamp": formated_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": developer.phone_number,
        "PartyB":"174379",
        "PhoneNumber": "254769624433",
        "CallBackURL": "https://react-django-qiy2.onrender.com",
        "AccountReference": "1234",
        "TransactionDesc": "real estate payments",
    }
    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


# pay_for_rental(request)

def register_call_back_url(request):

    my_access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        "ShortCode": '600996',
        "ResponseType": "Completed",
        "ConfirmationURL": "https://mysterious-oasis-16355.herokuapp.com/api/payments/c2b-confirmation/",
        "ValidationURL":   "https://mysterious-oasis-16355.herokuapp.com/api/payments/c2b-validation/",
    }

    try:
        response = requests.post(api_url, json=request, headers=headers)
    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)

    print(response.text)

    register_call_back_url()