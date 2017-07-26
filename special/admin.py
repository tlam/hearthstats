# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from special.forms import SpecialForm
from special.models import Special


class SpecialAdmin(admin.ModelAdmin):
    form = SpecialForm

admin.site.register(Special, SpecialAdmin)
