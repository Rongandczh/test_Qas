import pytest
from scripts.weather_api_script import WeatherApi


class TestWeather(object):

    def test_weather_api_is_work(self) :
        wea = WeatherApi()
        status_code = wea.check_status()
        assert status_code == 200

    def test_the_relative_humidity(self):
        wea = WeatherApi()
        res = wea.extract_the_relative_humidity()