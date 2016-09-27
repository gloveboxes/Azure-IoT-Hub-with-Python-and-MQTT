#!/bin/bash
echo "starting IoT Hub Client"

sleep 10

sudo killall python3

cd /home/pi/iothub/weather_mqtt

python3 weather_mqtt.py "config_envirophat.json"&
python3 weather_mqtt.py "config_sensehat.json"&

