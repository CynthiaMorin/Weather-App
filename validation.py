class Validation:
    @staticmethod
    def validate_city(city: str) -> bool:
        return city.isalpha() and len(city) > 1

    @staticmethod
    def validate_date(date: str) -> bool:
        try:
            # Simple YYYY-MM-DD validation
            year, month, day = map(int, date.split('-'))
            return 1 <= month <= 12 and 1 <= day <= 31
        except ValueError:
            return False
