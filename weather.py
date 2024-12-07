import requests
from typing import Dict, Optional

class WeatherAPI:
    # Base URL for the OpenWeatherMap API to get weather data
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
    # API key for authenticating requests (replace with your actual API key)
    API_KEY = "731b11a6fc004fcb5b9f4791ee38c462"  

    def get_weather(self, city: str, state: str, num_days: int) -> Optional[Dict]:
        """
        Fetches a 3-hour weather forecast for a specific city and state.

        Args:
            city (str): The name of the city for the forecast.
            state (str): The state abbreviation (e.g., 'CA', 'TX') for the city.
            num_days (int): The number of days for which the forecast is requested.

        Returns:
            dict | None: A dictionary containing the weather forecast data if the request is successful, 
                         or None if there is an error.
        """
        location = f"{city},{state},US"  # Construct the location string (e.g., 'City,State,US')
        params = {
            "q": location,  # Location query for the API
            "cnt": num_days * 8,  # 8 readings per day (3-hour intervals), so multiply by num_days
            "appid": self.API_KEY,  # API key for authentication
            "units": "metric",  # Use 'metric' for temperature in Celsius, 'imperial' for Fahrenheit
        }
        
        try:
            # Make the API request with the provided parameters
            response = requests.get(self.BASE_URL, params=params)
            # Raise an exception if the request failed (4xx or 5xx status codes)
            response.raise_for_status()
            # Return the JSON data from the response
            return response.json()
        except requests.RequestException as e:
            # If there's an error with the request, print the error message
            print(f"Error fetching data: {e}")
            return None
