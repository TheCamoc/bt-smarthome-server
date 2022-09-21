from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins, generics, renderers
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from backend.serializers import UserSerializer, GroupSerializer, DeviceSerializer, SwitchSerializer, RoomSerializer, \
    LightSerializer
from backend.models import Device, Switch, Room, Light


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
