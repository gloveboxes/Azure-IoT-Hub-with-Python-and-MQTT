import sys
import owm 
from sense_hat import SenseHat

class Sensor():
    sense = SenseHat()
    pubColour = (255,0,255)
    id = 0
    sensorLocation = ''
    openWeather = ''
    msg_txt = "{\"Geo\":\"%s\",\"Humidity\":%d,\"HPa\":%d,\"Celsius\": %.2f,\"Light\":%d,\"Id\":%d}"
   
    def __init__(self, owmApiKey, owmLocation='Sydney, au', cacheSeconds=60):
        self.openWeather = owm.Weather(owmApiKey, owmLocation)
        self.sensorLocation = owmLocation


    def measure(self):
        self.sense.clear(self.pubColour)

        self.openWeather.getWeather()
        lightlevel = 0
        self.id += 1     

        json = self.msg_txt % (self.sensorLocation, self.sense.get_humidity(), round(self.sense.get_pressure(),2), round(self.sense.get_temperature(),2), lightlevel, self.id)
        
        self.sense.clear()
        return json