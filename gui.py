import tkinter as tk
from datetime import datetime
from weather import WeatherAPI  # Assuming the WeatherAPI class is defined elsewhere
import json
from validation import Validation  # Assuming a Validation class is available

class TravelAppGUI:
    def __init__(self) -> None:
        """Initializes the main window for the application."""
        self.root = tk.Tk()
        self.root.title("Weather Wizard")
        self.root.geometry("600x400")  # Set the initial window size
        self.root.resizable(False, False)  # Disable resizing of the window

        # Initialize the weather result label as None (to be updated later)
        self.weather_result_label = None

        # Set up the home screen layout
        self.setup_home()

    def setup_home(self) -> None:
        """Sets up the initial home screen with welcome text and an 'Add Trip' button."""
        # Welcome label
        tk.Label(self.root, text="Welcome to Weather Wizard!", font=("Arial", 16)).pack(pady=10)
        
        # Instructional subheader
        subheader = tk.Label(
            self.root, 
            text="To fetch the weather forecast for your upcoming trip, click on 'Add Trip' below and enter your trip details.",
            font=("Arial", 12),
            wraplength=400,
            justify="center"
        )
        subheader.pack(pady=10)

        # 'Add Trip' button that triggers adding trip details
        tk.Button(self.root, text="Add Trip", command=self.add_trip).pack(pady=5)

        # Label to display weather data or errors
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
        """
        Validates the trip details and fetches the weather data for the given city and state.
        
        Args:
            city_entry (tk.Entry): The text entry widget for the city.
            state_entry (tk.Entry): The text entry widget for the state.
        """
        city = city_entry.get()
        state = state_entry.get().strip().upper()

        # Validate the city and state input
        if not city or not state:
            self.display_error("City and state are required!")
            return

        if state not in Validation.VALID_STATES:
            self.display_error("Invalid state format. Use 2-letter uppercase state abbreviations (e.g., FL, CA).")
            return

        # Fetch weather data using the WeatherAPI class
        weather_api = WeatherAPI()
        weather_data = weather_api.get_weather(city, state, 5)

        # If no valid data is returned, show an error
        if not weather_data or "list" not in weather_data:
            self.display_error("Could not fetch weather data. Try again!")
            return

        # Process and format the weather data
        forecast_text = f"Weather forecast for {city}, {state}:\n"
        daily_data = {}  # Dictionary to store aggregated daily data

        for forecast in weather_data["list"]:
            # Convert the timestamp to a readable date
            date_time = datetime.fromtimestamp(forecast["dt"])
            date = date_time.strftime("%Y-%m-%d")

            # Initialize daily data if it's a new day
            if date not in daily_data:
                daily_data[date] = {"max": float("-inf"), "min": float("inf")}

            # Get temperature data and convert it from Celsius to Fahrenheit
            if "main" in forecast:
                temp_max = forecast["main"].get("temp_max", daily_data[date]["max"])
                temp_min = forecast["main"].get("temp_min", daily_data[date]["min"])

                temp_max_fahrenheit = (temp_max * 9/5) + 32
                temp_min_fahrenheit = (temp_min * 9/5) + 32

                daily_data[date]["max"] = max(daily_data[date]["max"], temp_max_fahrenheit)
                daily_data[date]["min"] = min(daily_data[date]["min"], temp_min_fahrenheit)

        # Format the forecast text for the next 5 days
        for date, temps in sorted(daily_data.items())[:5]:  # Only show the next 5 days
            day_of_week = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
            forecast_text += f"{day_of_week} ({date}): High: {temps['max']:.1f}°F, Low: {temps['min']:.1f}°F\n"

        # Update the label with the weather forecast
        self.weather_result_label.config(text=forecast_text, fg="cyan")
        self.weather_result_label.update_idletasks()

    def display_error(self, message: str) -> None:
        """Displays an error message in red on the weather result label."""
        if self.weather_result_label:
            self.weather_result_label.config(text=message, fg="red")

    def run(self) -> None:
        """Starts the tkinter main loop to run the application."""
        self.root.mainloop()
