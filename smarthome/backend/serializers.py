from django.contrib.auth.models import User, Group
from rest_framework import serializers
from backend.models import Device, Switch, Room


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['url', 'name']


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ['url', 'name']


class SwitchSerializer(serializers.HyperlinkedModelSerializer):
    room_name = serializers.CharField(source='room.name', read_only=True)

    class Meta:
        model = Switch
        fields = ['url', 'name', 'state', 'mqtt_topic', 'room_name']
        read_only_fields = ['name', 'mqtt_topic', 'room_name']
