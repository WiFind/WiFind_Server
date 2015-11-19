# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursecall', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='id',
        ),
        migrations.AlterField(
            model_name='device',
            name='mac_addr',
            field=models.CharField(max_length=17, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(to='nursecall.Patient', null=True),
        ),
    ]
