from extract import get_weather_data
from datetime import datetime

def transform_weather_data():
    """Cleans and organizes the raw weather data"""
    raw_data = get_weather_data()
    
    if raw_data is None:
        print("❌ Data not found, cannot transform")
        return None
    
    # Extract only the required information
    transformed = {
        "city": raw_data["name"],
        "temperature_celsius": raw_data["main"]["temp"],
        "feels_like_celsius": raw_data["main"]["feels_like"],
        "humidity_percent": raw_data["main"]["humidity"],
        "weather_description": raw_data["weather"][0]["description"],
        "wind_speed": raw_data["wind"]["speed"],
        "recorded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    print("\n✅ Data transformed successfully:")
    for key, value in transformed.items():
        print(f"  {key}: {value}")
    
    return transformed

if __name__ == "__main__":
    transform_weather_data()