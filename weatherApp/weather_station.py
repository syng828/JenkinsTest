

class WeatherStation:
    def __init__(self):
        self.data = []

    def collect_data(self, temperature, humidity, wind_speed):
        data_entry = {
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
        self.data.append(data_entry)

    def analyze_data(self):
        # Placeholder for data analysis logic
        pass

    def display_data(self):
        for entry in self.data:
            print(f"Temperature: {entry['temperature']} | Humidity: {entry['humidity']} | Wind Speed: {entry['wind_speed']}")

# Instantiate the WeatherStation
weather_station = WeatherStation()
