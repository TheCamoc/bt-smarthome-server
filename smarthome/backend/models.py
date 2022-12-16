from json import JSONDecodeError
from decimal import InvalidOperation
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

    class Meta:
        verbose_name_plural = "Switches"


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


class Sensor(Device):
    mqtt_topic = models.CharField(max_length=100)
    temperature = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    humidity = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    pressure = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    air_quality = models.PositiveSmallIntegerField(blank=True, null=True)


def on_message(cl, userdata, msg):
    topic = msg.topic
    try:
        payload = json.loads(msg.payload)
        device = Sensor.objects.filter(mqtt_topic=topic).first()
        if device is not None:
            if "temperature" in payload:
                device.temperature = payload["temperature"]
            if "humidity" in payload:
                device.humidity = payload["humidity"]
            if "pressure" in payload:
                device.pressure = payload["pressure"]
            if "air_quality" in payload:
                device.air_quality = payload["air_quality"]
            device.save()
    except JSONDecodeError as e:
        print("JSON Decode Error: ", e.msg)
    except InvalidOperation as e:
        print("Decimal Invalid Operation: ", e)


mqtt.client.on_message = on_message
