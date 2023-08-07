import requests
TEQUILA_KEY ='a-7WNns8p9KTpojry2ZlUUPAccafEZpB'
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
class FlightData:
    
    #This class is responsible for structuring the flight data.
    def __init__(self, price,city_from_iata,city_from,city_to_iata,city_to,leave,arrive) -> None:
        self.price = price
        self.city_from = city_from
        self.city_from_iata = city_from_iata
        self.city_to = city_to
        self.city_to_iata = city_to_iata
        self.leave = leave
        self.arrive = arrive
        print(self.price)
        print(self.city_from)
        print(self.city_to)
        print(self.city_from_iata)
        print(self.city_to_iata)
        print(self.leave)
        print(self.arrive)
        