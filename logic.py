import requests
from typing import Dict, Optional
import json #I decided to use JSON for this data file because it's an easy and convenient way to store data. I learned how to use JSON in Python here: https://thenewstack.io/python-for-beginners-how-to-use-json-in-python/"""


class DataManager:
    """class for handling/managing data"""
    #Defining the file paths
    USER_FILE = "data/users.json"
    TRIP_FILE = "data/trips.json"

    @staticmethod #Learned how to use @staticmethod here: https://www.youtube.com/watch?app=desktop&v=7428SmlYD4M&t=140s
    def load_data(file_path: str) -> dict:
        """
        This function loads the data from the JSON file and returns it as a dictionary. file_path is the path to the JSON file I'm calling to be loaded.
        Should return a dictionary containing the loaded data, or an empty dictionary if an error occurs.
        """
        try:
            # Opening the file in read mode
            with open(file_path, 'r') as file:
                # json.load reads the JSON data from the file and converts it into a Python dictionary
                return json.load(file) #if all goes well, returns the JSON file as a dictionary
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file is not found or is not a valid JSON file, return an empty dictionary
            return {}

    @staticmethod #Learned how to use @staticmethod here: https://www.youtube.com/watch?app=desktop&v=7428SmlYD4M&t=140s
    def save_data(file_path: str, data: dict) -> None:
        """
        This function saves the provided data that we converted to a dictionary back to a JSON file. file_path in this function is
        the path to the JSON file where the data should be saved and data (dict) saves the data in the JSON file.
        This function does not return any value since it writes data to the file.
        """
        # Opening the file in write mode
        with open(file_path, 'w') as file:
            # json.dump writes the dictionary to the file, formatting it with indents for readability
            json.dump(data, file, indent=4)


class WeatherAPI:
    """class for fetching weather data/API"""
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

class Validation:
    """class to validate user inputs are acceptable"""
    # Set of valid US state abbreviations that will be used to validate user input
    VALID_STATES = {
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
        "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
        "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    }

    @staticmethod
    def validate_city(city: str) -> bool:
        """
        Validates that the city name contains only letters and is not too short.
        Returns boolean result; True if the city name is valid (only letters and at least 2 characters long), False otherwise.
        """
        return city.isalpha() and len(city) > 1


    @staticmethod
    def validate_state(state: str) -> bool:
        """
        Validates that the state abbreviation is one of the valid US state abbreviations.
        Returns boolean result; True if the state abbreviation is valid, False otherwise.
        """
        return state.upper() in Validation.VALID_STATES

