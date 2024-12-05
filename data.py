import json
#I decided to use json for this data file because it makes storing things easy within the data functions.
#I learned how to use json here: https://thenewstack.io/python-for-beginners-how-to-use-json-in-python/

class DataManager:
    USER_FILE = "data/users.json"
    TRIP_FILE = "data/trips.json"

    @staticmethod
    #Using the static method decorator so that the following load_data and save_data functions do not have access to the class attributes or class methods;
    #I learned how to use static methods here: https://www.youtube.com/watch?app=desktop&v=7428SmlYD4M&t=140s
    def load_data(file_path: str) -> dict:
        """saves the dictionary to the json file"""
        #str and dict in line 12 indicate that we are expecting a string input for the city, and that the function is to return a dictionary
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
            """json.load is parsing the json content to convert it into a python dictionary"""
        except (FileNotFoundError, json.JSONDecodeError):
            """error handling if the file was not in correct json format"""
            return {}

    @staticmethod
    def save_data(file_path: str, data: dict) -> None:
        """writes the data to the json file"""
        #str and dict in line 23 indicate that we are expecting a string input for the city, and that the function is to return a dictionary;
        #because the function is meant to store data/write it in the file, I set the output as none so it does not return a value
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
