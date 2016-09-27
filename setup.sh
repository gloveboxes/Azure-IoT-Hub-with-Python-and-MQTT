#!/bin/bash

echo Setting up Azure IoT Hub Python/MQTT Client Startup Services

chmod +x install_libraries.sh
sudo chmod +x startiot.sh

./install_libraries.sh


sudo cp iot.service /etc/systemd/system

sudo systemctl enable iot.service
sudo systemctl start iot.service
sudo systemctl status iot.service
