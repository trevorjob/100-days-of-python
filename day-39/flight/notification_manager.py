import requests
import datetime as dt

from twilio.rest import Client
account_sid = "AC432d529261c943b35a841d281db3b3d5"
auth_token = "a00c75e55258ee09dfefbb63687624a5"
class NotificationManager:
    def send_message(self):

        client = Client(account_sid, auth_token)
        message = client.messages.create(
                             body=f"message to be sent",
                             from_='+17623095622',
                             to='+2348104899622'
                         )
        print(message.status)
