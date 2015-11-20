# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursecall', '0004_auto_20151120_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='map_url',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
