# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursecall', '0005_auto_20151120_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='map_url',
            field=models.URLField(default=b'', max_length=300),
        ),
    ]
