import threading
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
            self.city_result.update({city: result_api.json()})
        else:
            self.city_result.update({"error": result_api.text})

    def collect_data(self):

        threads = []
        for i in range(100):
            for city in self.cities:
                thread = threading.Thread(target=self._call_api, args=(city,))
                threads.append(thread)
                thread.start()

        for thread in threads:
            thread.join()


start = datetime.now()

a = ApiCollector(constans.WEATHER_API_URL, cities)

end = datetime.now()

print(end - start)
# print(a.city_result)
