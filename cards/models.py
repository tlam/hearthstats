import json
import pprint
import os

from django.conf import settings
from django.db import models


SETS = ['Classic', u'Curse of Naxxramas', 'Basic', 'Reward', 'Goblins vs Gnomes']

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

        num_owned = 0
        total = 0
        for card in cards:
            num_owned += card.count
            total += card.max_count
        return total, cards.count(), num_owned

    @property
    def max_count(self):
        if self.elite:
            return 1
        else:
            return 2

    def image_url(self):
        return 'http://wow.zamimg.com/images/hearthstone/cards/enus/original/{}.png'.format(self.hearthstone_id)
