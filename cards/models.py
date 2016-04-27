from collections import OrderedDict
import json
import pprint
import os

from django.conf import settings
from django.db import models


SETS = ['Classic', 'Goblins vs Gnomes', 'The Grand Tournament', 'Whispers of the Old God']

class Card(models.Model):
    name = models.CharField(max_length=255, unique=True)
    cost = models.IntegerField(default=0)
    card_type = models.CharField(max_length=255, default='')
    rarity = models.CharField(max_length=255, default='')
    faction = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255, blank=True, default='')
    mechanics = models.CharField(max_length=255, blank=True, default='')
    flavour = models.CharField(max_length=255, blank=True, default='')
    attack = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    elite = models.BooleanField(default=False)
    set_name = models.CharField(max_length=255, default='')
    hearthstone_id = models.CharField(max_length=255, unique=True)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u'{}'.format(self.name)

    @staticmethod
    def grand_total(set_name=''):
        if set_name:
            cards = Card.objects.filter(set_name=set_name)
        else:
            cards = Card.objects.all()

        rarity = [
            ('Common', {'own': 0, 'total': 0}),
            ('Rare', {'own': 0, 'total': 0}),
            ('Epic', {'own': 0, 'total': 0}),
            ('Legendary', {'own': 0, 'total': 0}),
        ]
        output = {
            'total_owned': 0,
            'rarity': OrderedDict(rarity),
            'total': 0,
        }
        for card in cards:
            if card.rarity in ['', 'Free']:
                continue
            output['rarity'][card.rarity]['own'] += card.count
            output['rarity'][card.rarity]['total'] += card.max_count
            output['total_owned'] += card.count
            output['total'] += card.max_count

        output['distinct_total'] = cards.count()
        return output

    @property
    def max_count(self):
        if self.elite:
            return 1
        else:
            return 2

    def image_url(self):
        return 'http://wow.zamimg.com/images/hearthstone/cards/enus/original/{}.png'.format(self.hearthstone_id)
