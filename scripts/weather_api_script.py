import requests
import json
from datetime import datetime, timedelta

class WeatherApi(object):

    host = "https://data.weather.gov.hk"

    def check_status(self):
        uri = "/weatherAPI/opendata/weather.php?dataType={0}&lang={1}"
        _dataType = "fnd"
        _lang = "tc"
        uri = uri.format(_dataType,_lang)
        res = requests.get(url=self.host+uri)
        print('Success, The status code is {0}'.format(res.status_code))
        return res.status_code


    def extract_the_relative_humidity(self):
        uri = "/weatherAPI/opendata/weather.php?dataType={0}&lang={1}"
        _dataType = "fnd"
        _lang = "tc"
        uri = uri.format(_dataType,_lang)
        res = requests.get(url=self.host+uri)
        res = res.text
        res = json.loads(res)
        weatherForecast = res['weatherForecast']
        now = datetime.now()
        after_tmr = (now + timedelta(days=2)).strftime("%Y%m%d")
        for i in weatherForecast:
            if i['forecastDate'] == after_tmr:
                forecastMaxrh = i['forecastMaxrh']['value']
                foecastMinrh = i['forecastMinrh']['value']
                date = i['week']
        print('The day after tomorrow({0})\'s relative humidity is {1} - {2} %'.format(after_tmr, foecastMinrh, forecastMaxrh))
        
