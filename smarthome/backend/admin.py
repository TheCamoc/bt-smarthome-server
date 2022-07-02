from django.contrib import admin

from .models import Switch, Device, Room

admin.site.register(Room)
admin.site.register(Device)
admin.site.register(Switch)
