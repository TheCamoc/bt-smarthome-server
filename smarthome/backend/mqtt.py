import paho.mqtt.client as mqtt
import json


def on_connect(cl, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        client.subscribe("update")
        client.subscribe("ping")
        print("MQTT connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_message(cl, userdata, msg):
    topic = msg.topic
    print(msg)
    print("message received")

    # msg.append(m)#put messages in list
    # q.put(m) #put messages on queue
    # Do something .....


mqtt.Client.connected_flag = False
broker = "192.168.99.5"
client = mqtt.Client("backend")
client.on_connect = on_connect
client.on_message = on_message
# client.username_pw_set(username="your mqtt username", password="your mqtt password")
print("Connecting to broker ", broker)
client.connect(broker)
