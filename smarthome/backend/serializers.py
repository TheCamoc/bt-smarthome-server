from django.contrib.auth.models import User, Group
from rest_framework import serializers
from backend.models import Device, Switch, Room


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
