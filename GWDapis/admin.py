from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import WaterLevels, WaterQuality, GW_General

admin.site.register(GW_General)
admin.site.register(WaterQuality)
admin.site.register(WaterLevels)