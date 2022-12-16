from django.contrib import admin

from .models import Switch, Room, Light, Sensor

admin.site.register(Room)
admin.site.register(Switch)
admin.site.register(Light)
admin.site.register(Sensor)
