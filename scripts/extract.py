import requests
import os
from dotenv import load_dotenv

# Load the API key from the .env file.
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# Which city's data do you need
CITY = "Sialkot"

# Let's create the API URL.
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather_data():
    """A function that fetches weather data from an API."""
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        print("✅Data fetched successfully!")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        return data
    else:
        print(f"❌ Show Error: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    get_weather_data()
