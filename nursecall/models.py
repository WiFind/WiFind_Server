from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name


class Device(models.Model):
    mac_addr = models.CharField(max_length=17)
    owner = models.ForeignKey(Patient)
    notify = models.BooleanField(default=False)
    help_req = models.BooleanField(default=False)
    def __unicode__(self):
        return self.mac_addr
