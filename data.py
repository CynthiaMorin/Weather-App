import json

class DataManager:
    USER_FILE = "data/users.json"
    TRIP_FILE = "data/trips.json"

    @staticmethod
    def load_data(file_path: str) -> dict:
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    @staticmethod
    def save_data(file_path: str, data: dict) -> None:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
