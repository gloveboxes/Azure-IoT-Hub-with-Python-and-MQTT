# https://azure.microsoft.com/en-us/documentation/articles/iot-hub-mqtt-support/
# http://stackoverflow.com/questions/35452072/python-mqtt-connection-to-azure-iot-hub/35473777
# https://azure.microsoft.com/en-us/documentation/samples/iot-hub-python-get-started/


# Mqtt Support https://www.eclipse.org/paho/clients/python/
# pip3 install paho-mqtt

# Weather data Open Weather Map using https://github.com/csparpa/pyowm
# pip3 install pyowm

import paho.mqtt.client as mqtt
import time
import helper
import sys
import json

sensor = hubAddress = deviceId = sharedAccessKey = owmApiKey = owmLocation = None

def config_defaults():
    global sensor, hubAddress, deviceId, sharedAccessKey, owmApiKey, owmLocation
    print('Loading default config settings')

    import sensor_openweather as sensor
    hubAddress = 'IoTCampAU.azure-devices.net'
    deviceId = 'mqtt'
    sharedAccessKey= 'VZbmLwYjjdg04Gb5SvbNMTq44GdDEO5k5px6OUIu7l8='
    owmApiKey = 'c204bb28a2f9dc23925f27b9e21296dd'
    owmLocation = 'Melbourne, AU'

def config_load():
    global sensor, hubAddress, deviceId, sharedAccessKey, owmApiKey, owmLocation
    try:
        if len(sys.argv) == 2:
            print('Loading {0} settings'.format(sys.argv[1]))

            config_data = open(sys.argv[1])
            config = json.load(config_data)

            sensor = __import__(config['SensorModule']) 
            hubAddress = config['IotHubAddress']
            deviceId = config['DeviceId']
            sharedAccessKey = config['SharedAccessKey']
            owmApiKey = config['OpenWeatherMapApiKey']
            owmLocation = config['OpenWeatherMapLocationId']
        else:
            config_defaults()
    except:
        config_defaults()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: %s" % rc)
    client.subscribe(help.hubTopicSubscribe)

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code: %s" % rc)
    client.username_pw_set(help.hubUser, help.generate_sas_token(help.endpoint, sharedAccessKey))

def on_message(client, userdata, msg):
    print("{0} - {1} ".format(msg.topic, str(msg.payload)))
    # Do this only if you want to send a reply message every time you receive one
    # client.publish("devices/mqtt/messages/events", "REPLY", qos=1)

def on_publish(client, userdata, mid):
    print("Message {0} sent from {1}".format(str(mid), deviceId))

def publish():
    while True:
        try:
            client.publish(help.hubTopicPublish, mysensor.measure())            
            time.sleep(4)
        
        except KeyboardInterrupt:
            print("IoTHubClient sample stopped")
            return

        except:
            print("Unexpected error")
            time.sleep(4)

config_load()

mysensor = sensor.Sensor(owmApiKey, owmLocation)
help = helper.Helper(hubAddress, deviceId, sharedAccessKey)

client = mqtt.Client(deviceId, mqtt.MQTTv311)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.on_publish = on_publish

client.username_pw_set(help.hubUser, help.generate_sas_token(help.endpoint, sharedAccessKey))

#client.tls_set("/etc/ssl/certs/ca-certificates.crt") # use builtin cert on Raspbian
client.tls_set("baltimorebase64.cer") # Baltimore Cybertrust Root exported from Windows 10 using certlm.msc in base64 format
client.connect(hubAddress, 8883)

client.loop_start()

publish()
