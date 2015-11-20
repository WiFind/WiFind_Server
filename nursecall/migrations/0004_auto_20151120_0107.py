# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursecall', '0003_auto_20151120_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='map_url',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AddField(
            model_name='device',
            name='x_loc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='device',
            name='y_loc',
            field=models.IntegerField(default=0),
        ),
    ]
