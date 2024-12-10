import json

#I decided to use JSON for this data file because it's an easy and convenient way to store data. I learned how to use JSON in Python here: https://thenewstack.io/python-for-beginners-how-to-use-json-in-python/"""

class DataManager:
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
