from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Device, Switch, Room, Light, Sensor, Fan, Thermostat, Table


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['url', 'name']


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['url', 'name']


class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = ['url', 'name', 'state', 'mqtt_topic', 'room']
        read_only_fields = ['name', 'mqtt_topic', 'room']


class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = ['url', 'name', 'state', 'mqtt_topic', 'room', 'r', 'g', 'b', 'w', 'has_white_led']
        read_only_fields = ['name', 'mqtt_topic', 'room', 'has_white_led']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['url', 'name', 'mqtt_topic', 'room', 'temperature', 'humidity', 'pressure', 'air_quality']
        read_only_fields = ['name', 'mqtt_topic', 'room']


class ThermostatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thermostat
        fields = ['url', 'name', 'mqtt_topic', 'room', 'target_temperature', 'state']
        read_only_fields = ['name', 'mqtt_topic', 'room']


class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fan
        fields = ['url', 'name', 'state', 'speed', 'mqtt_topic', 'room']
        read_only_fields = ['name', 'mqtt_topic', 'room']


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['url', 'name', 'state', 'mqtt_topic', 'room']
        read_only_fields = ['name', 'mqtt_topic', 'room']
