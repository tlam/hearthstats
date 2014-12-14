# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20141214_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='hearthstone_id',
            field=models.CharField(default='', unique=True, max_length=255),
            preserve_default=False,
        ),
    ]
