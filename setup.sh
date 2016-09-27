#!/bin/bash

echo Setting up Azure IoT Hub Python/MQTT Client Startup Services


sudo pip3 install pyowm
sudo pip3 install paho-mqtt


sudo chmod +x startiot.sh


sudo cp iot.service /etc/systemd/system

sudo systemctl enable iot.service
sudo systemctl start iot.service
sudo systemctl status iot.service
