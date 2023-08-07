##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import  random
import pandas

MY_EMAIL = 'redeks123456@gmail.com'
TO_EMAIL = 'jobkumdan@gmail.com'
PASSWORD = "mqwsczyzlmhtbltd"
CURRENT = dt.datetime.now()
DATA = pandas.read_csv('birthdays.csv').to_dict(orient='records')

# 1. Update the birthdays.csv


# 2. Check if today matches a birthday in the birthdays.csv
def is_there_birthday():
        for bday in DATA:
                if CURRENT.day == bday['day'] and CURRENT.month == bday['month']:
                        return bday
        return None
        
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def get_letter():
        with open(f'./letter_templates/letter_{random.randint(1,3)}.txt', 'r') as file:
                new_file = file.read().replace('[NAME]', BIRTHDAY['name']).replace('Angela', 'Nandom')
                return new_file
        
# 4. Send the letter generated in step 3 to that person's email address.
def send_letter(letter):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=f"Subject:HAPPY BIRTHDAY\n\n{letter}")
                connection.close()

BIRTHDAY = is_there_birthday()        
if BIRTHDAY is not None:
        LETTER = get_letter()
        send_letter(LETTER)

