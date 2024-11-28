import requests

class WeatherAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "731b11a6fc004fcb5b9f4791ee38c462"  # Replace with your API key

    @staticmethod
    def get_weather(city: str) -> dict:
        try:
            response = requests.get(WeatherAPI.BASE_URL, params={"q": city, "appid": WeatherAPI.API_KEY})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather: {e}")
            return {}
 