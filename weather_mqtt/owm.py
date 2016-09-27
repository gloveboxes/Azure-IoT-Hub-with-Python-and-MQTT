import pyowm
import time
import json

class Weather():

    def __init__(self, owmApiKey, owmLocation='Sydney, au', cacheSeconds=60):
        self._owm = pyowm.OWM(owmApiKey)  # You MUST provide a valid API key
        self.owmLocation = owmLocation
        if cacheSeconds < 0:
            self._cacheSeconds = 60
        else:
            self._cacheSeconds = cacheSeconds


    temperature = 0
    humidity = 0
    pressure = 0
    owmLocation = ''

    _cacheSeconds = 0
    _lastWeatherRequest = time.time() - 60000
   
    def config(self):
        print('Open Weather Map Loaction: ' + self.owmLocation)


    def getWeather(self):
        try:
            if self._lastWeatherRequest + self._cacheSeconds < time.time():
                self._lastWeatherRequest = time.time()
                
                observation = self._owm.weather_at_place(self.owmLocation)
                w = observation.get_weather()

                temp = w.get_temperature('celsius')
                self.humidity = w.get_humidity()                
                press = w.get_pressure()

                j = json.dumps(temp)
                o = json.loads(j)
                self.temperature = o['temp']

                j = json.dumps(press)
                o = json.loads(j)
                self.pressure = o['press']
        except:
            print("open weather call failed")



