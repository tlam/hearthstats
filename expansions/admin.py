# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from expansions.models import Expansion


class ExpansionAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date',)

admin.site.register(Expansion, ExpansionAdmin)
