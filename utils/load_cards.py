import collections

import requests

from cards.models import Card
from expansions.models import Expansion


class LoadCards(object):

    def process(self):
        url = 'https://api.hearthstonejson.com/v1/latest/enUS/cards.collectible.json'
        response = requests.get(url)
        data = response.json()

        expansions = collections.OrderedDict()
        for expansion in Expansion.objects.all():
            expansions[expansion.code] = expansion.name
        count = 0
        for card in data:
            if card['set'] in expansions:
                cards = Card.objects.filter(name=card['name'])
                if cards.count() == 1:
                    continue

                Card.objects.create(
                    name=card['name'],
                    cost=card['cost'],
                    card_type=card['type'].title(),
                    rarity=card['rarity'].title(),
                    description=card.get('text', ''),
                    flavour=card['flavor'],
                    attack=card.get('attack', 0),
                    health=card.get('health', 0),
                    elite='LEGENDARY' == card['rarity'],
                    set_name=expansions[card['set']],
                    hearthstone_id=card['id'],
                )
                count += 1

        return count
