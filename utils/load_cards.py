from datetime import datetime
import collections

import requests

from cards.models import Card
from expansions.models import Expansion


class LoadCards(object):
    INVALID_CARD_TYPES = ['HERO']

    def process(self):
        url = 'https://api.hearthstonejson.com/v1/latest/enUS/cards.collectible.json'
        response = requests.get(url)
        data = response.json()

        expansions = collections.OrderedDict()
        for expansion in Expansion.objects.all():
            expansions[expansion.code] = expansion.name
        count = 0
        for card in data:
            if card['type'] in self.INVALID_CARD_TYPES:
                continue

            if card.get('set') in expansions:
                cards = Card.objects.filter(name=card['name'])
                if cards.count():
                    continue

                Card.objects.create(
                    name=card['name'],
                    cost=card.get('cost', 0),
                    card_type=card['type'].title(),
                    rarity=card['rarity'].title(),
                    description=card.get('text', ''),
                    flavour=card.get('flavor', ''),
                    attack=card.get('attack', 0),
                    health=card.get('health', 0),
                    elite='LEGENDARY' == card['rarity'],
                    set_name=expansions[card['set']],
                    hearthstone_id=card['id'],
                )
                count += 1

        return count

    def create_expansion(self, name):
        Expansion.objects.get_or_create(
            code=name,
            defaults={'name': name, 'release_date': datetime.now()}
        )
