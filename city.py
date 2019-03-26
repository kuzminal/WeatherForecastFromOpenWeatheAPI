import pprint
import requests
from dateutil.parser import parse


class OpenWeather:

    def get(self, city):
        url = f"https://api.openweathermap.org/data/2.5/forecast?q=Moscow,RU&appid=22e18f12088ac290c6163e4824c95847"
        data = requests.get(url).json()
        forecast_data = data["list"]
        forecast = []
        for day_data in forecast_data:
            forecast.append({
                "date": parse(day_data["dt_txt"]),
                "high_temp": day_data["main"]["temp"]
            })
        return forecast

class CityInfo:

    def __init__(self, city, weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or OpenWeather()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)

def _main():
    city_info = CityInfo("Moscow")
    forecast = city_info.weather_forecast()
    pprint.pprint(forecast)

if __name__ == "__main__":
    _main()