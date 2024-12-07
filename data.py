import json

"""I decided to use JSON for this data file because it's an easy and convenient way to store data.
I learned how to use JSON in Python here: https://thenewstack.io/python-for-beginners-how-to-use-json-in-python/"""

class DataManager:
    # Constants to define the file paths
    USER_FILE = "data/users.json"
    TRIP_FILE = "data/trips.json"

    @staticmethod
    def load_data(file_path: str) -> dict:
        """
        Loads the data from a JSON file and returns it as a dictionary.
        
        Args:
            file_path (str): The path to the JSON file to be loaded.
        
        Returns:
            dict: A dictionary containing the loaded data, or an empty dictionary if an error occurs.
        """
        try:
            # Opening the file in read mode
            with open(file_path, 'r') as file:
                # json.load reads the JSON data from the file and converts it into a Python dictionary
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file is not found or is not a valid JSON file, return an empty dictionary
            return {}

    @staticmethod
    def save_data(file_path: str, data: dict) -> None:
        """
        Saves the provided data (a dictionary) to a JSON file.

        Args:
            file_path (str): The path to the JSON file where the data should be saved.
            data (dict): The data to be saved in the JSON file.
        
        Returns:
            None: This function does not return any value as it writes data to the file.
        """
        # Opening the file in write mode
        with open(file_path, 'w') as file:
            # json.dump writes the dictionary to the file, formatting it with indents for readability
            json.dump(data, file, indent=4)
