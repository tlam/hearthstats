# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Special(models.Model):
    card_id = models.IntegerField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return u'{}'.format(self.title)
