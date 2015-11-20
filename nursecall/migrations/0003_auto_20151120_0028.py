# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursecall', '0002_auto_20151119_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(blank=True, to='nursecall.Patient', null=True),
        ),
    ]
