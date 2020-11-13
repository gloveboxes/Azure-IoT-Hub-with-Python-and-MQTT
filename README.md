# Azure IoT Hub with Python and MQTT support from Windows, Mac OS X Sierra, Linux including Ubuntu and Raspberry Pi Zero, 2 and 3

This cross platform Python3 code sample demonstrates how to stream data to Azure IoT Hub from Windows, OSX, Linux including Ubuntu and Raspberry Pi Zero, 2 and 3

As at September 2016.

## Language: Python3

## Tested Platforms

1. Windows 10, but any version of Windows running Python3 should work
2. Apple OSX, tested on 10.12 Sirri Release, but any version of OSX running Python3 should work
3. Linux
    * Windows (10) Subsystem for Linux (Ubuntu 14.04)
    * Ubuntu 16.04
4. Rasperry Pi, Raspbian Kernel 4.4 fully patched. 
    * Raspbrry Pi Zero
    * Raspberry Pi 2
    * Raspberry Pi 3
5. Should work on any platform supporting Python3 and the Paho-Mqtt library.

# Installation

Easiest way is to git clone the solution.

        git clone https://github.com/gloveboxes/Azure-IoT-Hub-with-Python-and-MQTT.git iothub

then change to the iothub directory.

    cd iothub

On Windows run

    install_libraries.bat to install the required pip3 libraries

On Raspberry Pi run

    ./setup.sh

This will also setup the solution to autorun at startup

This also 

On Apple Mac

    pip3 install pyowm
    pip3 install paho-mqtt


# Library Support

1. Paho-MQTT
    * pip3 install paho-mqtt
2. Open Weather Map for Virtual Weather HAT
    * pip3 pyowm

# Raspberry Pi HATS

Sample code includes support for the following HATS

1. [Raspberry Pi Sense HAT](https://www.raspberrypi.org/products/sense-hat/): sensor_envirophat.py
2. [Enviro pHAT](https://shop.pimoroni.com/products/enviro-phat): sensor_sensehat
3. [Open Weather Map](http://openweathermap.org/) sensor_openweather.py

# Startup Configuration

Pass in a configuration .json file at run time.

example sensor_envirophat.json

    {
    "IotHubAddress":"YourIoTHub.azure-devices.net",
    "DeviceId":"pizero",
    "SharedAccessKey":"uJ21qp9LUvjkohipkXycvb7RoYwmUDE+4gXyIYS00feZg=",
    "SensorModule":"sensor_envirophat",
    "OpenWeatherMapApiKey":"c2044448a2f55555925f27b9e21296dd",
    "OpenWeatherMapLocationId":"Melbourne, AU"
    }

## Startup example

    python3 weather_mqtt.py sensor_envirophat.json
    python3 weather_mqtt.py sensor_openweather.json


# MQTT TLS Certificate

On Linux 
    
    client.tls_set("/etc/ssl/certs/ca-certificates.crt") # use builtin cert on Raspbian

On Windows using certlm.msc export one of the top level public certificate authority keys such as the Baltimore Cybertrust Root to a .cer file in base64 format.

    client.tls_set("baltimorebase64.cer") # Baltimore Cybertrust Root exported from Windows 10 using certlm.msc in base64 format

The sample includes the Baltimore Cybertrust Key exported as baltimorebase64.cer that can be used across platforms.

# Recommended Software

1. To find your Raspberry Pi on your network by name install [Apple Print Bonjour Service](https://support.apple.com/kb/dl999?locale=en_AU) on Windows for mDNS UNIX Name Resolution. .
2. My favourite SSH and SFTP Windows Client is [Bitvise](https://www.bitvise.com/)
3. [Visual Studio Code](https://code.visualstudio.com/?WT.mc_id=iot-0000-dglover) for Windows, Mac and Linux


# Tips and Tricks

### Visual Studio Code, Python3 and OSX

From [Debugging Python 3.x with Visual Studio Code on OSX](https://nocture.dk/2016/05/07/debugging-python-3-x-with-visual-studio-code-on-osx/)

OSX comes with Python 2.x by default, and setting the default Python version to 3.x is not without trouble. Here is how you debug Python 3.x applications with Visual Studio Code and the Python extension.

1. Open the application folder in VS Code 
2. Create a new launch configuration based on the Python template 
3. Add "pythonPath": "/Library/Frameworks/Python.framework/Versions/3.5/bin/python3" to the configuration so that it looks similar to the following: 

    {
        "name": "Python",
        "type": "python",
        "request": "launch",
        "pythonPath": "/Library/Frameworks/Python.framework/Versions/3.5/bin/python3",
        "stopOnEntry": true,
        "program": "${file}",
        "debugOptions": [
            "WaitOnAbnormalExit",
            "WaitOnNormalExit",
            "RedirectOutput"
        ]
    }

**And start debugging!**

### Handy Tip for Raspberry Pi Zero

[Raspberry Pi Zero – Programming over USB](http://blog.gbaman.info/?p=791) ONLY works with Raspberry Pi Zero and provides a quick easy way to connect your PC to your Raspberry Pi Zero.


# Setting up Python3 on Mac OS X

This is mainly for my benefit as I have limited experience with an apple mac.

1. Install [Python3](www.python3.org)
2. Update [Tcl/Tk for Idle3](www.python.org/download/mac/tcltk). Install ActiveTcl 8.5.18.0.








