import tkinter as tk
from datetime import datetime, timedelta
from travel import Trip
from weather import WeatherAPI

class TravelAppGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather Wizard")

        # Initialize weather result label early
        self.weather_result_label = None

        # Main layout
        self.setup_home()

    def setup_home(self):
        tk.Label(self.root, text="Welcome to Weather Wizard!", font=("Arial", 16)).pack(pady=10)
        subheader = tk.Label(self.root, text="To fetch the weather forecast for your upcoming trip, click on 'Add Trip' below and enter your trip details.", font=("Arial", 12), wraplength=400, justify="center")
        subheader.pack(pady=10)

        # Add Trip Button
        tk.Button(self.root, text="Add Trip", command=self.add_trip).pack(pady=5)

        # Create and initialize a label to display weather results or errors
        self.weather_result_label = tk.Label(self.root, text="", font=("Arial", 12), wraplength=300)
        self.weather_result_label.pack(pady=10)

    def add_trip(self):
        def submit_trip():
            city = city_entry.get()
            start_date = start_date_entry.get()
            end_date = end_date_entry.get()

            if not city or not start_date or not end_date:
                self.display_error("All fields are required!")
                return

            try:
                start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
                today = datetime.today()
                max_forecast_date = today + timedelta(days=16)

                if start_date_obj < today or end_date_obj < today:
                    self.display_error("Dates are in the past, please try again")
                    return

                if start_date_obj > max_forecast_date or end_date_obj > max_forecast_date:
                    self.display_error(
                        "Sorry, but weather checker can only check the forecast up to 16 days from now. Please try again"
                    )
                    return

            except ValueError:
                self.display_error("Invalid date format. Please use YYYY-MM-DD.")
                return

            # Weather fetching logic
            weather_api = WeatherAPI()
            weather = weather_api.get_weather(city)

            if weather and "weather" in weather:
                trip = Trip(city, start_date, end_date)
                trip.set_weather(weather)

                description = weather['weather'][0]['description']
                temperature = weather['main']['temp'] - 273.15
                self.weather_result_label.config(
                    text=f"Weather in {city}: {description.capitalize()}, {temperature:.1f}°C",
                    fg="green",
                )
            else:
                self.display_error("Could not fetch weather data. Try again!")

        # Create a new frame within the main window for input
        trip_frame = tk.Frame(self.root)
        trip_frame.pack(pady=10)

        tk.Label(trip_frame, text="City:").grid(row=0, column=0, padx=5, pady=5)
        city_entry = tk.Entry(trip_frame)
        city_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(trip_frame, text="Start Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        start_date_entry = tk.Entry(trip_frame)
        start_date_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(trip_frame, text="End Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        end_date_entry = tk.Entry(trip_frame)
        end_date_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(trip_frame, text="Submit", command=submit_trip).grid(row=3, columnspan=2, pady=10)

    def display_error(self, message: str):
        """Displays an error message in red on the weather_result_label."""
        if self.weather_result_label:  # Ensure label exists
            self.weather_result_label.config(text=message, fg="red")

    def run(self):
        self.root.mainloop()
