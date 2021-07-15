-------------------------------------------------------------------------------------------------------------------------------------------
IMPORT MY DOCKER MQTT IMAGE:
1. unzip the given file, inside you will find a tar file. Move that into kali.
2. load docker image with the following command
	docker load -i <path to image tar file>
3. Run mqtt docker with the following command:
	docker run --cap-add=NET_ADMIN -it --rm --hostname iot-mqtt --net iot_network --ip 172.19.0.12 -v iot_vol:/root/iot_vol --name iot-mqtt yusuf-iot-mqtt bash
-------------------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------------------------------------------------------
RUNNING MQTT FOR PRODUCTION:
1. unzip the given file, inside you will find "iotsec". Drop the "iotsec" folder inside the "/root/iot_vol/" directory.
2. cd into "/root/iot_vol/iotsec/cacert/crt/" and enter the following command:
	mosquitto -c mosquitto.conf -v

RUNNING THE MQTT LISTENER AKA (mqtt.py)
0. For this you would need another terminal sesssion to the container. User docker exec.
1. unzip the given file, inside you will find "iotsec". Drop the "iotsec" folder inside the "/root/iot_vol/" directory.
2. cd into "/root/iot_vol/iotsec/" and enter the following command:
	python mqtt.py
-------------------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------------------------------------------------------
Add this in your sensor code to be able to interact and send data to MQTT with SSL(done)!

import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.tls_set('/root/iot_vol/iotsec/cacert/crt/ca.crt')
mqttc.username_pw_set("cost", password="cost")
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))		

		
def publishToTopic(topic, message):
	mqttc.publish(topic,message)
	print ("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print("")


def mqttUpdate(appliance, statusappliance, shadeCovered, editedBy, topic):
	Data = {}
	Data['appliance'] = appliance
	Data['status'] = statusappliance
	Data['shadeCovered'] = shadeCovered
	Data['editedBy'] = editedBy
	DataJson = json.dumps(Data)
	print("Publishing data to mqtt... ")
	publishToTopic(topic, DataJson)
-------------------------------------------------------------------------------------------------------------------------------------------