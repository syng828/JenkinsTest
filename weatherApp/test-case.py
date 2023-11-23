import pytest
from weather_station import WeatherStation

@pytest.fixture
def weather_station_instance():
    return WeatherStation()

def test_collect_data(weather_station_instance):
    weather_station_instance.collect_data(25, 50, 10)
    assert len(weather_station_instance.data) == 1

def test_analyze_data(weather_station_instance):
    # Placeholder for data analysis test
    pass

def test_display_data(capsys, weather_station_instance):
    weather_station_instance.collect_data(25, 50, 10)
    weather_station_instance.display_data()
    captured = capsys.readouterr()
    assert "Temperature: 25 | Humidity: 50 | Wind Speed: 10" in captured.out
