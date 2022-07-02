from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Device(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.RESTRICT)


class Switch(Device):
    state = models.BooleanField()
    mqtt_topic = models.CharField(max_length=100)
