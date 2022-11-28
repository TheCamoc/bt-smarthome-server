from django.db import models
from django.db.models import UniqueConstraint

from . import mqtt
import json


class Room(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    class Meta:
        constraints = [
            UniqueConstraint(fields=['name', 'room'], name='unique_device')
        ]

    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.RESTRICT)

    def __str__(self):
        return "{0}: {1}".format(self.room, self.name)


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
