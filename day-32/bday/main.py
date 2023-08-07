import smtplib
import datetime as dt
import  random

my_email = 'redeks123456@gmail.com'
to_email = 'jobkumdan@gmail.com'
password = "mqwsczyzlmhtbltd"
#
# # connection = smtplib.SMTP("smtp.gmail.com", 587)
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=to_email, msg="Subject:Hello\n\nthis is the body of the email")
#     connection.close()

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# print(year, month, day, now.weekday())
#
# date_of_birth = dt.datetime(year=2003, month=6, day=21, hour=12)
# print(date_of_birth)

current = dt.datetime.now()

if current.weekday() == 1:
    with open(file='quotes.txt', mode='r') as quotes:
        quotes = quotes.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Motivational Quote\n\n{quote}")
        connection.close()
