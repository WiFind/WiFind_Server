from django.contrib import admin

# Register your models here.

from .models import Patient, Device

admin.site.register(Patient)
admin.site.register(Device)
