from django.db import models
from . import mqtt
import json

class Room(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Device(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.RESTRICT)


class Switch(Device):
    state = models.BooleanField()
    mqtt_topic = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        mqtt.client.publish(self.mqtt_topic, json.dumps({"state": self.state}))
        super().save(*args, **kwargs)
