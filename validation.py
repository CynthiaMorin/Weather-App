class Validation:
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
