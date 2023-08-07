import requests
from pprint import pprint
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.url = 'https://api.sheety.co/124440079d8326a98eeb48b4aec6826e/deals/prices'
    
    def update_iata(self,destin,data):
        sheety_req = requests.put(url=f'{self.url}/{destin}', json=data)
    
    def get_request(self):
        sheety_req = requests.get(url=self.url)
        sheet = sheety_req.json()
        print(sheet)
        return sheet