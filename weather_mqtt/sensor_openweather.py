import sys
#sys.path[0:0] = ['../common'] ## path to shared owm.py (open weather map) and iothub.py (azure iot hub python) files
import owm 

class Sensor():
    id = 0
    sensorLocation = ''
    openWeather = ''
    msg_txt = "{\"Geo\":\"%s\",\"Humidity\":%d,\"HPa\":%d,\"Celsius\": %.2f,\"Light\":%d,\"Id\":%d}"
   
    def __init__(self, owmApiKey, owmLocation='Sydney, au', cacheSeconds=60):
        self.openWeather = owm.Weather(owmApiKey, owmLocation)
        self.sensorLocation = owmLocation


    def measure(self):
        self.openWeather.getWeather()
        lightLevel = 0
        self.id += 1
        return self.msg_txt % (self.sensorLocation, self.openWeather.humidity, self.openWeather.pressure, self.openWeather.temperature, lightLevel, self.id)
