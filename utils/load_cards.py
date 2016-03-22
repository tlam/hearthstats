import requests

from cards.models import Card, SETS
from utils import constants


class LoadCards(object):

    def process(self):
        url = 'https://api.hearthstonejson.com/v1/latest/enUS/cards.collectible.json'
        response = requests.get(url)
        data = response.json()

        sets = set()
        count = 0
        for card in data:
            if card['set'] in constants.SETS_MAP:
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
                    elite='LENGENDARY' == card['rarity'],
                    set_name=constants.SETS_MAP[card['set']],
                    hearthstone_id=card['id'],
                )
                count += 1

        return count
