import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from cards.models import Card


class Command(BaseCommand):

    def handle(self, *args, **options):
        fp = open(os.path.join(settings.BASE_DIR, 'cards', 'fixtures', 'collection.json'))
        data = json.loads(fp.read())
        fp.close()

        for entry in data:
            try:
                card = Card.objects.get(name=entry['name'])
                card.count = entry['count']
                card.save()
            except Card.DoesNotExist:
                print '{} does not exist'.format(entry['name'])
