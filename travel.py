from typing import List, Dict

class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.trips = []

    def add_trip(self, trip) -> None:
        self.trips.append(trip)

class Trip:
    def __init__(self, destination: str, start_date: str, end_date: str):
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.weather = {}

    def set_weather(self, weather: Dict):
        self.weather = weather
