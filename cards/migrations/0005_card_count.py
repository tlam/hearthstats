# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_card_hearthstone_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
