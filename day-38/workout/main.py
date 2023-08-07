import requests
from datetime import datetime
import os
APPID = 'fa4ec799'
APIKEY = os.environ.get('NUT_APPID')
print(APIKEY)
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


headers = {
        "x-app-id" :APPID,
        "x-remote-user-id":"0",
        "x-app-key":APIKEY,
}

user_params = {
        'query' : input("what do u do: "),
        'gender': 'male',
        'weight_kg': '80',
        'height_cm': '182.88',
        'age': '20',
}
response = requests.post(url=endpoint, json=user_params, headers=headers)
response.raise_for_status()
result = response.json()

print(result)

# SHEETY_API = "https://api.sheety.co/124440079d8326a98eeb48b4aec6826e/works/workouts"

# now = datetime.now()
# tim = now.strftime('%X')
# nn = now.strftime("%d/%m/%Y")

# # exercise_list = []
# # for exe in result['exercises']:
# #     exercise_data = {
# #         "date": nn,
# #         "exercise": exe["name"].title(),
# #         "duration": exe["duration_min"],
# #         "time": tim,
# #         "calories": exe["nf_calories"],
# #     }
# #     exercise_list.append(exercise_data)

# # sheety_params = {
# #     "workout": exercise_list
# # }

# # sheety_response = requests.post(url=SHEETY_API, json=sheety_params)
# # sheety_response.raise_for_status()
# # print(sheety_response.text)


# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")

# sheet_inputs = {
#         "workout": {
#             "date": today_date,
#             "time": now_time,
#             "exercise": result["exercises"][0]["name"].title(),
#             "duration": result["exercises"][0]["duration_min"],
#             "calories": result["exercises"][0]["nf_calories"]
#         }
# }

# sheet_response = requests.post(url=SHEETY_API, json=sheet_inputs)

# print(sheet_response.text)