# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20141214_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
