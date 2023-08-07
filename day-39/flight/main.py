from pprint import pprint

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
data = DataManager()
flightsearch = FlightSearch()
sheet_data = data.get_request()
print(sheet_data)
# for sheet in sheet_data['prices']:
#         code = flightsearch.get_iata(sheet['city'])        
#         sheet['iataCode'] = code
#         data.update_iata(sheet['id'],{'price':sheet})
#         resp = flightsearch.search_flight(sheet['iataCode'], sheet['lowestPrice'])

noti = NotificationManager()
noti.send_message()
