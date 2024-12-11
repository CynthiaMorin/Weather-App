import requests
from typing import Dict, Optional

class WeatherAPI:
    # URL for the OpenWeatherMap API to get weather data
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
    # API key for authenticating requests, generated from OpenWeatherMap website (replace with your actual API key, you will need to create an account)
    API_KEY = "731b11a6fc004fcb5b9f4791ee38c462"  

    def get_weather(self, city: str, state: str) -> Optional[Dict]:
        """
        Fetches the forecast for a specific city and state as input.
        Returns a dictionary containing the weather forecast data if the request is successful, or None if there is an error.
        """
        location = f"{city},{state},US"  # Construct the location string (e.g., 'City,State,US')
        params = {
            "q": location,  # Location query for the API
            "appid": self.API_KEY,  # API key for authentication
            "units": "metric",  # Uses 'metric' for temperature in Celsius, since that is what OpenWeatherMap uses, will convert it later
        }
        
        try:
            # Makes the API request to OpenWeatherMap with the provided parameters
            response = requests.get(self.BASE_URL, params=params)
            # Raises an exception if the request from the user fails 
            response.raise_for_status()
            # Returns the JSON data from the response from OpenWeatherMap
            return response.json()
        except requests.RequestException as e:
            # If there's an error with the request, print the error message
            print(f"Error fetching data: {e}")
            return None
