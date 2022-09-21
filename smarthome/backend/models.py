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


class Light(Device):
    state = models.BooleanField()
    mqtt_topic = models.CharField(max_length=100)
    has_white_led = models.BooleanField()
    r = models.PositiveSmallIntegerField()
    g = models.PositiveSmallIntegerField()
    b = models.PositiveSmallIntegerField()
    w = models.PositiveSmallIntegerField()

    def save(self, *args, **kwargs):
        mqtt.client.publish(self.mqtt_topic, json.dumps(
            {
                "state": self.state,
                "r": self.r,
                "g": self.g,
                "b": self.b,
                "w": self.w
            }
        ))
        super().save(*args, **kwargs)
