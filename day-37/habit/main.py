import requests
import datetime as dt
pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'nandom'
TOKEN = 'blessedacademy'
user_params = {
        'token':TOKEN,
        'username':USERNAME,
        'agreeTermsOfService': 'yes',
        'notMinor':'yes'
}
# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
        'id': "graph1",
        'name': "reading graph",
        "unit": "page",
        "type": "int",
        'color': "kuro"
}
headers = {
        'X-USER-TOKEN':TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

post_graph_endpoint = f"{graph_endpoint}/{graph_config['id']}"
now = dt.datetime.now()
year = str(now.year)
month = str(now.month)
day = str(now.day)
date = f"{year}{month if int(month) >= 10 else month.zfill(2)}{day if int(day) >= 10 else day.zfill(2)}"
post_config = {
        "date": "20230622",
        'quantity': '10'
}
# response = requests.post(url=post_graph_endpoint, json=post_config, headers=headers)

# nn = now.strftime("%Y%m%d")

put_graph_endpoint = f"{post_graph_endpoint}/{post_config['date']}"
put_config = {
        'quantity': '50'
}
# response = requests.put(url=put_graph_endpoint, json=put_config, headers=headers)


response = requests.delete(url=put_graph_endpoint,headers=headers)
print(response.text)