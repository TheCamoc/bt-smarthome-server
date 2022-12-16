import paho.mqtt.client as mqtt
import sys
import random


def on_connect(cl, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        client.subscribe("#")
        print("MQTT connected OK")
    else:
        print("Bad connection Returned code=", rc)


mqtt.Client.connected_flag = False
broker = "127.0.0.1"
client = mqtt.Client("backend{0}".format(random.randint(0, 200)))
client.on_connect = on_connect

if 'smarthome.wsgi:application' in sys.argv:
    print("Connecting to broker ", broker)
    client.connect(broker)
