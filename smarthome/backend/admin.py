from django.contrib import admin

from .models import Switch, Room, Light, Sensor, Thermostat, Fan

admin.site.register(Room)
admin.site.register(Switch)
admin.site.register(Light)
admin.site.register(Sensor)
admin.site.register(Thermostat)
admin.site.register(Fan)
