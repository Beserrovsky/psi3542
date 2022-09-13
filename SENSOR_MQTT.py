import random
import time
import json
import math
from paho.mqtt import client as mqtt_client

ORG = "ss4bdu"
DEVICE_TYPE = "raspi" 
TOKEN = "m@(1(?JaFbNgdEM+pU"
DEVICE_ID = "5ccd5b930001"

server = ORG + ".messaging.internetofthings.ibmcloud.com"
topic = "iot-2/evt/status1/fmt/json"
authmethod = "use-token-auth"
token = TOKEN
clientid = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID
port = 1883

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(clientid)
    client.username_pw_set(authmethod, token)
    client.on_connect = on_connect
    client.connect(server, port)
    return client


def publish(client):
    msg_count = 0
    ang=0
    while True:
        time.sleep(1)
        temperature = (math.sin(ang) * 50) + 50
        humidity = random.gauss(80.0, 5)
        
        ang+=0.1

        msg = {'d':{'temperature': temperature, 'humidity': humidity}} # f"messages: {msg_count}"
        result = client.publish(topic, json.dumps(msg))
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
