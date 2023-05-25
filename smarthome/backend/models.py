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


class Thermostat(Device):
    state = models.BooleanField()
    mqtt_topic = models.CharField(max_length=100)
    target_temperature = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
    rel_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        mqtt.client.publish(self.mqtt_topic, json.dumps({"state": self.state}))
        super().save(*args, **kwargs)


class Fan(Device):
    state = models.BooleanField()
    speed = models.PositiveSmallIntegerField()
    mqtt_topic = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.state:
            mqtt.client.publish(self.mqtt_topic, json.dumps({"value": self.state}))
        else:
            mqtt.client.publish(self.mqtt_topic, json.dumps({"value": 0}))
        super().save(*args, **kwargs)


def on_message(cl, userdata, msg):
    topic = msg.topic
    try:
        payload = json.loads(msg.payload)
        sensor = Sensor.objects.filter(mqtt_topic=topic).first()
        if sensor is not None:
            if "temperature" in payload:
                sensor.temperature = payload["temperature"]
            if "humidity" in payload:
                sensor.humidity = payload["humidity"]
            if "pressure" in payload:
                sensor.pressure = payload["pressure"]
            if "air_quality" in payload:
                sensor.air_quality = payload["air_quality"]
            sensor.save()

        thermostat = Thermostat.objects.filter(rel_sensor=sensor).first()
        if thermostat is not None and sensor.temperature is not None:
            new_state = None
            if sensor.temperature < (thermostat.target_temperature - 1):
                new_state = True
            elif sensor.temperature > (thermostat.target_temperature + 1):
                new_state = False

            if new_state is not None and new_state != thermostat.state:
                thermostat.state = new_state
                thermostat.save()
    except JSONDecodeError as e:
        print("JSON Decode Error: ", e.msg)
    except InvalidOperation as e:
        print("Decimal Invalid Operation: ", e)


mqtt.client.on_message = on_message
