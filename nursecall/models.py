from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name


class Device(models.Model):
    mac_addr = models.CharField(max_length=17, primary_key=True)
    owner = models.ForeignKey(Patient, null=True, blank=True)
    notify = models.BooleanField(default=False)
    help_req = models.BooleanField(default=False)
    x_loc  = models.IntegerField(default=0)
    y_loc = models.IntegerField(default=0)
    map_url = models.CharField(max_length=500, default='')
    def __unicode__(self):
        return self.mac_addr
