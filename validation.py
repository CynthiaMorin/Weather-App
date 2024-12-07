class Validation:
    # Set of valid US state abbreviations
    VALID_STATES = {
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
        "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
        "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    }

    @staticmethod
    def validate_city(city: str) -> bool:
        """
        Validates that the city name contains only letters and is not too short.
        
        Args:
            city (str): The name of the city to be validated.

        Returns:
            bool: True if the city name is valid (only alphabetic characters and at least 2 characters long), 
                  False otherwise.
        """
        return city.isalpha() and len(city) > 1

    @staticmethod
    def validate_date(date: str) -> bool:
        """
        Validates that the given date is in the format YYYY-MM-DD and contains valid month and day values.
        
        Args:
            date (str): The date string to be validated.

        Returns:
            bool: True if the date is in a valid format and the month and day are within valid ranges, 
                  False otherwise.
        """
        try:
            year, month, day = map(int, date.split('-'))
            # Check if the month and day are valid
            return 1 <= month <= 12 and 1 <= day <= 31
        except ValueError:
            # Return False if there is an error in the date format or conversion
            return False

    @staticmethod
    def validate_state(state: str) -> bool:
        """
        Validates that the state abbreviation is one of the valid US state abbreviations.
        
        Args:
            state (str): The state abbreviation to be validated.

        Returns:
            bool: True if the state abbreviation is valid, False otherwise.
        """
        return state.upper() in Validation.VALID_STATES
