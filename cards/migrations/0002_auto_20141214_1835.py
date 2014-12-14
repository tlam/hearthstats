# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='attack',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='description',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='elite',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='faction',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='flavour',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='health',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='mechanics',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='rarity',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='set_name',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
