import requests
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth

def timestamp():
    unformatted_time=datetime.now()#2024-03-23
    formated_time=unformatted_time.strftime("%Y%m%d%H%M%S")#"20240323"
    return formated_time
    

def password(formated_time):
    #  Shortcode+Passkey+Timestamp bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919
    data_to_encode="174379" + "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919" + formated_time

    encoded_password=base64.b64encode(data_to_encode.encode())

    decoded_password=encoded_password.decode('utf-8')
    print('password'+ decoded_password)
    return decoded_password



def generate_access_token():
   
    consumer_key = "Fd4KnnG0lPHXhBnBAZoMshaOR2BFZ1ru1EGa96GOW9gcYR3Q"
    consumer_secret = "VfjoJpsuSLaTjNHI3qUohkt6B6ND3l16GJMdXR9gbrURcGe1BJWDPoHLv7WbqHFA"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
  
    try:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    except:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret), verify=False)
        
    print(r.text)
   
    json_response = (r.json())  

    my_access_token = json_response["access_token"]
   
    return my_access_token



def register_call_back_url():

    my_access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % my_access_token}

    request = {
        "ShortCode": '600978',
        "ResponseType": "Completed",
        "ConfirmationURL": "https://13a6-102-212-11-22.ngrok-free.app/pay_rental",
        "ValidationURL":   "https://13a6-102-212-11-22.ngrok-free.app/pay_rental",
    }

    try:
        response = requests.post(api_url, json=request, headers=headers)
    except:
        response = requests.post(api_url, json=request, headers=headers, verify=False)

    print(response.text)
    print(my_access_token)
   
    
    
def pay_for_rental():
    
    formated_time = timestamp()
 
    access_token = generate_access_token()
    
 
          
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % access_token}

    request_data = {
            "BusinessShortCode": "174379",
            "Password": password(formated_time),
            "Timestamp": formated_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",
            "PartyA": '254769624433',
            "PartyB": "174379",
            "PhoneNumber": "254769624433",
            "CallBackURL": "https://react-django-qiy2.onrender.com/pay_rental",
            "AccountReference": "1234",
            "TransactionDesc": "real estate payments",
        }

    response = requests.post(api_url, json=request_data, headers=headers)

    print(response.text)


pay_for_rental()





