from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins, generics, renderers
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer, GroupSerializer, DeviceSerializer, SwitchSerializer, RoomSerializer, \
    LightSerializer, SensorSerializer, FanSerializer, ThermostatSerializer, TableSerializer
from .models import Device, Switch, Room, Light, Sensor, Fan, Thermostat, Table


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and modify Rooms
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and modify Devices
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class SwitchViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and modify Switches
    """
    queryset = Switch.objects.all()
    serializer_class = SwitchSerializer


class LightViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and modify Lights
    """
    queryset = Light.objects.all()
    serializer_class = LightSerializer


class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and modify Lights
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ThermostatViewSet(viewsets.ModelViewSet):
    """
        API endpoint to view and modify Lights
        """
    queryset = Thermostat.objects.all()
    serializer_class = ThermostatSerializer


class FanViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and modify Fans
    """
    queryset = Fan.objects.all()
    serializer_class = FanSerializer


class TableViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view and modify Fans
    """
    queryset = Table.objects.all()
    serializer_class = TableSerializer