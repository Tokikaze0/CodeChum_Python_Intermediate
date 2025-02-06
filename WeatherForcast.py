import requests
import logging

# Configure logging
logging.basicConfig(filename="weather_app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class WeatherFetcher:
    """Fetches weather data from Open-Meteo API."""
    API_URL = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, latitude, longitude):
        """Fetch weather data for given coordinates."""
        try:
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": True
            }
            response = requests.get(self.API_URL, params=params)
            response.raise_for_status()  # Raise error if request fails
            data = response.json()
            logging.info(f"Successfully fetched weather data for coordinates ({latitude}, {longitude})")
            return data
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching weather data: {e}")
            print(f"Error: {e}")  # Debugging
            return None

class WeatherReport(WeatherFetcher):
    """Generates and displays a weather report."""
    
    def display_weather(self, latitude, longitude):
        """Fetch and display formatted weather information."""
        data = self.get_weather(latitude, longitude)
        if data and "current_weather" in data:
            weather = data["current_weather"]
            print(f"\nWeather Report for Coordinates ({latitude}, {longitude})")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Wind Speed: {weather['windspeed']} km/h")
            print(f"Weather Code: {weather['weathercode']}")
        else:
            print("Failed to retrieve weather data. Please try again.")

if __name__ == "__main__":
    # Replace with actual coordinates or get user input
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    weather_app = WeatherReport()
    weather_app.display_weather(latitude, longitude)
