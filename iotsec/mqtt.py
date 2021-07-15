import paho.mqtt.client as mqtt
import json
import requests
import ssl
ssl.match_hostname = lambda cert, hostname: True

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("Cost/Sensors")


def on_message(client, userdata, message):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + message.topic + " " + str(message.payload))  # Print a received msg
    jsonData = (message.payload).decode('utf-8')
    json_Dict = json.loads(jsonData)
    appliance = json_Dict['appliance']
    #print(appliance)

    if appliance == "Kupton Retractable Patio Shade":
        status = json_Dict['status']
        shadeCovered = json_Dict['shadeCovered']
        editedBy = json_Dict['editedBy']
        print(message.topic)
        print(appliance)
        print(status)
        print(shadeCovered)
        print(editedBy)
        urlLive = "http://172.19.0.13:8080/add/" + "kuptonShade" + "?status=" + status + "&covered=%s" %shadeCovered + "&editedBy=" + editedBy
        urlLogs = "http://172.19.0.13:8080/add/" + "kuptonShade" + "?status=" + status + "&covered=%s" %shadeCovered + "&editedBy=" + editedBy
        print(urlLive) 
        #print(requests.put(urlLive))
        print(urlLogs) 
        #print(requests.put(urlLogs))

while True:
    client = mqtt.Client("cost")
    client.on_connect = on_connect
    client.on_message = on_message
    client.tls_set('/root/iot_vol/iotsec/cacert/crt/ca.crt')
    client.username_pw_set("cost", password="cost")
    client.connect('172.19.0.12', 1883)
    client.loop_forever()