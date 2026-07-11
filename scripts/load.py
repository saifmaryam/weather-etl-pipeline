import psycopg2
from transform import transform_weather_data

def create_table(cursor):
    """Creates the table if it doesn't already exist"""
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            temperature_celsius FLOAT,
            feels_like_celsius FLOAT,
            humidity_percent INT,
            weather_description VARCHAR(200),
            wind_speed FLOAT,
            recorded_at TIMESTAMP
        );
    """)
    print("✅ Table is ready (or already existed)")

def load_weather_data():
    """Loads the transformed weather data into PostgreSQL"""

    # Get the transformed data first
    data = transform_weather_data()

    if data is None:
        print("❌ No data available, cannot load")
        return

    # Connect to the database
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="weather_db",
        user="postgres",
        password="weather123"
    )
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    create_table(cursor)

    # Insert the data
    cursor.execute("""
        INSERT INTO weather_data 
        (city, temperature_celsius, feels_like_celsius, humidity_percent, weather_description, wind_speed, recorded_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        data["city"],
        data["temperature_celsius"],
        data["feels_like_celsius"],
        data["humidity_percent"],
        data["weather_description"],
        data["wind_speed"],
        data["recorded_at"]
    ))

    conn.commit()  # Save/confirm the changes
    print("✅ Data saved to the database!")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    load_weather_data()
