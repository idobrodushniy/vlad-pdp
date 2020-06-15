from datetime import datetime

import requests

import constans

cities = ["London", "Paris", "Barcelona", "New York", "Dublin", "Budapest"]


class ApiCollector:
    city_result = {}

    def __init__(self, url, cities):

        self.url = url
        self.cities = cities
        self.collect_data()

    def _call_api(self, city):

        result_api = requests.get(self.url.format(city=city))

        if result_api.status_code == 200:
            return result_api.json()
        else:
            return {"error": result_api.text}

    def collect_data(self):
        for i in range(100):
            for city in cities:
                self.city_result.update({city: self._call_api(city)})


start = datetime.now()

a = ApiCollector(constans.WEATHER_API_URL, cities)

end = datetime.now()

print(end - start)
