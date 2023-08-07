import requests
import os
from twilio.rest import Client
API_KEY = '6e6df90dee7e0103aaf90c6d58b8a226'
account_sid = "AC432d529261c943b35a841d281db3b3d5"
auth_token = "a00c75e55258ee09dfefbb63687624a5"


client = Client(account_sid, auth_token)


message = client.messages \
                .create(
                     body="how far na how things na",
                     from_='+17623095622',
                     to='+2348104899622'
                 )
print(message.sid)


# parameters = {'lat': 6.5833, 'lon':3.75, 'appid':API_KEY}
# response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)


# API_KEY = '6e6df90dee7e0103aaf90c6d58b8a226'
# parameters = {'q':'Lagos', 'appid':API_KEY}
# response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)