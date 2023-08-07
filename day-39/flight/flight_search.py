import requests
from pprint import pprint
from flight_data import FlightData

from datetime import datetime, timedelta
now = datetime.now()
six_months_from_now = now + timedelta(days=6*30)
nn = now.strftime("%d/%m/%Y")
six = six_months_from_now.strftime("%d/%m/%Y")
TEQUILA_KEY ='a-7WNns8p9KTpojry2ZlUUPAccafEZpB'
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
class FlightSearch:
    
    def search_flight(self, city, price):
        endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {'apikey': TEQUILA_KEY}
        params = {
            'fly_from': 'LON',
            'fly_to': city,
            'date_from':nn,
            'date_to':six,
            'curr':'GBP',
            'price_to':price,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            }
        response = requests.get(url=endpoint, headers=headers, params=params)
        try:
            data = response['data'][0]
        except:
            print(f'No flights found for {city}')
            return None
        
        flightdata = FlightData(data['price'], data['flyFrom'], data['cityFrom'], data['flyTo'], data['cityTo'], data['utc_departure'].split('T'), data['utc_arrival'].split('T'))
        
        return flightdata
    
    def get_iata(self,city):
        endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {'apikey': TEQUILA_KEY}
        params = {'term':city,"location_types": "city"}
        response = requests.get(url=endpoint, headers=headers, params=params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
    
    
    
        