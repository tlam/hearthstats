from django.contrib import admin

from cards.models import Card


class CardAdmin(admin.ModelAdmin):
    list_filter = ('set_name',)
    search_fields = ['name']

admin.site.register(Card, CardAdmin)
