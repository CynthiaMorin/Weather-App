from typing import List, Dict

class User:
    def __init__(self, user_id: int, name: str) -> None:
        """
        Initializes a new user with an ID and name, and initializes an empty list of trips.
        
        Args:
            user_id (int): The unique identifier for the user.
            name (str): The name of the user.
        """
        self.user_id = user_id
        self.name = name
        self.trips: List[Trip] = []  # List to store trips associated with the user

    def add_trip(self, trip: 'Trip') -> None:
        """
        Adds a trip to the user's list of trips.
        
        Args:
            trip (Trip): An instance of the Trip class to be added to the user's trip list.
        """
        self.trips.append(trip)


class Trip:
    def __init__(self, destination: str, start_date: str, end_date: str) -> None:
        """
        Initializes a trip with a destination, start date, end date, and an empty weather dictionary.
        
        Args:
            destination (str): The destination of the trip.
            start_date (str): The start date of the trip.
            end_date (str): The end date of the trip.
        """
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.weather: Dict[str, float] = {}  # Dictionary to store weather data for the trip

    def set_weather(self, weather: Dict[str, float]) -> None:
        """
        Sets the weather data for the trip.
        
        Args:
            weather (Dict[str, float]): A dictionary containing weather data (e.g., temperature).
        """
        self.weather = weather
