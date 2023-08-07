import requests
import datetime as dt

from twilio.rest import Client
account_sid = "AC432d529261c943b35a841d281db3b3d5"
auth_token = "a00c75e55258ee09dfefbb63687624a5"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "ZJ9O2QFVS80ZSC80"
NEWS_API_KEY = '7b5632143abb4b149aee0e94e716e716'

cur_date = str(dt.datetime.now())
day = int(cur_date[8:10]) - 3
cur_date = cur_date[:8]

def perc(num_a, num_b):
    return (num_a / num_b) * 100
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def stock_price():
        global difference
        stock_parameters = {'function': 'TIME_SERIES_DAILY', 'symbol':STOCK, 'apikey':STOCK_API_KEY}
        stock_response = requests.get('https://www.alphavantage.co/query', params=stock_parameters)
        stock_response.raise_for_status()
        
        data = stock_response.json()["Time Series (Daily)"]
        data_list = [value for (key, value) in data.items()]
        yesterday_data = data_list[0]
        yesterday_closing_price = yesterday_data["4. close"]
        print(yesterday_closing_price)

        #Get the day before yesterday's closing stock price
        day_before_yesterday_data = data_list[1]
        day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
        print(day_before_yesterday_closing_price)

        dif = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
        if perc(abs(dif), float(yesterday_closing_price)) > 1:
                return dif, True
        else:
                return False, False



# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
        news_parameters = {'q': COMPANY_NAME, 'apiKey':NEWS_API_KEY}
        news_response = requests.get('https://newsapi.org/v2/everything', params=news_parameters)
        news_response.raise_for_status()
        data = news_response.json()
        return [{'title':article['title'], 'description':article['description'], 'url':article['url']} for article in data['articles']]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_message():
        for new in news[:3]:
                client = Client(account_sid, auth_token)
                message = client.messages \
                                .create(
                                     body=f"{STOCK}: {'🔺' if difference > 0 else '🔻'}{int(abs(difference))}%\nHeadline: {new['title']}\nBrief: {new['description']}\n\nfor more info visit {new['url']}",
                                     from_='+17623095622',
                                     to='+2348104899622'
                                 )
                print(message.status)
                
difference, check = stock_price()

if check:
        news = get_news()
        if news:
                send_message()
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

