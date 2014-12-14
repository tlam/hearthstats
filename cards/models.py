import json
import pprint
import os

from django.conf import settings
from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=255, unique=True)
    cost = models.IntegerField(default=0)
    card_type = models.CharField(max_length=255, default='')
    rarity = models.CharField(max_length=255, default='')
    faction = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    mechanics = models.CharField(max_length=255, default='')
    flavour = models.CharField(max_length=255, default='')
    attack = models.IntegerField(default=0)
    health = models.IntegerField(default=0)
    elite = models.BooleanField(default=False)
    set_name = models.CharField(max_length=255, default='')
    hearthstone_id = models.CharField(max_length=255, unique=True)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return u'{}'.format(self.name)

    @staticmethod
    def load():
        fp = open(os.path.join(settings.BASE_DIR, 'cards', 'fixtures', 'AllSets.json'))
        data = json.loads(fp.read())
        fp.close()
        sets = ['Classic', u'Curse of Naxxramas', 'Basic', 'Reward', 'Goblins vs Gnomes']

        types = []
        for set_name, set_data in data.iteritems():
            if set_name not in sets:
                continue

            for card in set_data:
                if 'cost' not in card:
                    continue
                if Card.objects.filter(name=card['name']).count() == 1:
                    continue

                Card.objects.create(
                    name=card['name'],
                    cost=card['cost'],
                    card_type=card['type'],
                    rarity=card.get('rarity', ''),
                    faction=card.get('faction', ''),
                    description=card.get('text', ''),
                    mechanics=card.get('mechanics', ''),
                    flavour=card.get('flavor', ''),
                    attack=card.get('attack', 0),
                    health=card.get('health', 0),
                    elite='elite' in card,
                    set_name=set_name,
                    hearthstone_id=card['id'],
                )
