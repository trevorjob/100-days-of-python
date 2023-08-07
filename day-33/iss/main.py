import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = 'redeks123456@gmail.com'
PASSWORD = "mqwsczyzlmhtbltd"
MY_LAT =  6.524379 # Your latitude
MY_LONG =  3.379206 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


def iss_over():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    #If the ISS is close to my current position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        
        if (time_now.hour < sunrise) and (time_now.hour >= sunset):
            return True
        else:
            return False
    else:
        return False
# and it is currently dark
# Then send me an email to tell me to look up.

# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if iss_over():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:ISS IS OVER YOU\n\nquick go outside and look up the iss is over you")
            connection.close()

