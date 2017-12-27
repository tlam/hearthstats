from django.contrib import admin

from cards.models import Card


class CardAdmin(admin.ModelAdmin):
    list_filter = ('set_name',)
    list_display = ('name', 'count',)
    search_fields = ['name']


admin.site.register(Card, CardAdmin)
