# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Expansion(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    release_date = models.DateField()

    class Meta:
        ordering = ['release_date']

    def __unicode__(self):
        return u'{}'.format(self.name)
