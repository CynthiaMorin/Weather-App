import tkinter as tk
from datetime import datetime
from logic import WeatherAPI  # Calls WeatherAPI from weather module
import json
from logic import Validation  # Calls Validation from validation module

class TravelAppGUI:
    def __init__(self) -> None:
        """Initializes the main window for the application."""
        self.root = tk.Tk()
        self.root.title("Weather Wizard")
        self.root.geometry("600x400")  # Sets the initial window size
        self.root.resizable(False, False)  # Makes the window nonresizable

        # Initialize the weather result label as None; this gets updated later in this module
        self.weather_result_label = None

        # Sets up the home screen layout
        self.setup_home()

    def setup_home(self) -> None:
        """Sets up the initial home screen with welcome text and an 'Add Trip' button."""
        # Welcome label
        tk.Label(self.root, text="Welcome to Weather Wizard!", font=("Arial", 16)).pack(pady=10)
        
        # Instructions for user go here, along with all the formatting for that text
        subheader = tk.Label(
            self.root, 
            text="To fetch the weather forecast for your upcoming trip, click on 'Add Trip' below and enter your trip details.",
            font=("Arial", 12),
            wraplength=400,
            justify="center"
        )
        subheader.pack(pady=10)

        # 'Add Trip' button that triggers entry boxes for user inputs
        tk.Button(self.root, text="Add Trip", command=self.add_trip).pack(pady=5)

        # Label to display weather data or error messages
        self.weather_result_label = tk.Label(self.root, text="", font=("Arial", 12), wraplength=300)
        self.weather_result_label.pack(pady=10)

    def add_trip(self) -> None:
        """Creates a new frame for users to input city and state for their trip."""
        # Create and pack a new frame for input fields
        trip_frame = tk.Frame(self.root, pady=20)
        trip_frame.pack(fill="both", expand=True)  # Make the frame expand to fill space
        trip_frame.pack_propagate(False)  # Prevent resizing of the frame

        # Configure grid columns to be expandable
        trip_frame.grid_columnconfigure(0, weight=1)
        trip_frame.grid_columnconfigure(1, weight=1)

        # City input field
        city_label = tk.Label(trip_frame, text="City:", font=("Arial", 12))
        city_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        city_entry = tk.Entry(trip_frame, font=("Arial", 12), width=25)
        city_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # State input field
        state_label = tk.Label(trip_frame, text="State (e.g., CA):", font=("Arial", 12))
        state_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        state_entry = tk.Entry(trip_frame, font=("Arial", 12), width=10)
        state_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Submit button to submit trip details
        submit_button = tk.Button(trip_frame, text="Submit", font=("Arial", 12), command=lambda: self.submit_trip(city_entry, state_entry))
        submit_button.grid(row=2, columnspan=2, pady=15)  # Center the button

        # Force the window to update its layout
        self.root.update_idletasks()

    def submit_trip(self, city_entry: tk.Entry, state_entry: tk.Entry) -> None:
        """ Validates the trip details and fetches the weather data for the given city and state. """
        city = city_entry.get()
        state = state_entry.get().strip().upper()

        # Validate the city and state input from the validation tab
        if not city or not state:
            self.display_error("City and state are required!")
            return

        if state not in Validation.VALID_STATES: #Generates error if user inputs format incorrectly
            self.display_error("Invalid state format. Use 2-letter uppercase state abbreviations (e.g., FL, CA).")
            return

        # Fetch weather data using the WeatherAPI class
        weather_api = WeatherAPI()
        weather_data = weather_api.get_weather(city, state)

        # If no valid data is returned, shows an error
        if not weather_data or "list" not in weather_data:
            self.display_error("Could not fetch weather data. Try again!")
            return

        # Processes and formats the weather data
        forecast_text = f"Weather forecast for {city}, {state}:\n"
        daily_data = {}  # Dictionary that stores daily data

        for forecast in weather_data["list"]:
            # Convert the timestamp to a readable date using datetime
            date_time = datetime.fromtimestamp(forecast["dt"])
            date = date_time.strftime("%Y-%m-%d")

            # Initializes daily data if it's a new day
            if date not in daily_data:
                daily_data[date] = {"max": float("-inf"), "min": float("inf")}

            # Gets temperature data and converts it from Celsius to Fahrenheit, as the API fetches in Celsius
            if "main" in forecast:
                temp_max = forecast["main"].get("temp_max", daily_data[date]["max"])
                temp_min = forecast["main"].get("temp_min", daily_data[date]["min"])

                temp_max_fahrenheit = (temp_max * 9/5) + 32
                temp_min_fahrenheit = (temp_min * 9/5) + 32

                daily_data[date]["max"] = max(daily_data[date]["max"], temp_max_fahrenheit)
                daily_data[date]["min"] = min(daily_data[date]["min"], temp_min_fahrenheit)

        # Formats the forecast output text for the next 5 days
        for date, temps in sorted(daily_data.items())[:5]:  # Only show the next 5 days
            day_of_week = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
            forecast_text += f"{day_of_week} ({date}): High: {temps['max']:.1f}°F, Low: {temps['min']:.1f}°F\n"

        # Update the label with the weather forecast
        self.weather_result_label.config(text=forecast_text, fg="cyan")
        self.weather_result_label.update_idletasks()

    def display_error(self, message: str) -> None:
        """Displays an error message in red on the weather result label if an error occurs."""
        if self.weather_result_label:
            self.weather_result_label.config(text=message, fg="red")

    def run(self) -> None:
        """Starts the tkinter main loop to run the application."""
        self.root.mainloop()
