import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from cards.models import Card, SETS


class Command(BaseCommand):

    def handle(self, *args, **options):
        fp = open(os.path.join(settings.BASE_DIR, 'cards', 'fixtures', 'AllSets.json'))
        data = json.loads(fp.read())
        fp.close()

        for set_name, set_data in data.iteritems():
            if set_name not in SETS:
                continue

            for card in set_data:
                collectible = card.get('collectible', False)
                faction = card.get('faction', '')
                rarity = card.get('rarity', '')
                if 'cost' not in card or card['type'] == 'Hero Power' or (rarity == '' and faction == '') or not collectible:
                    continue

                cards = Card.objects.filter(name=card['name'])
                if cards.count() == 1:
                    continue

                Card.objects.create(
                    name=card['name'],
                    cost=card['cost'],
                    card_type=card['type'],
                    rarity=rarity,
                    faction=faction,
                    description=card.get('text', ''),
                    mechanics=card.get('mechanics', ''),
                    flavour=card.get('flavor', ''),
                    attack=card.get('attack', 0),
                    health=card.get('health', 0),
                    elite='elite' in card,
                    set_name=set_name,
                    hearthstone_id=card['id'],
                )
