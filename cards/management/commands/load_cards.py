import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from utils.load_cards import LoadCards


class Command(BaseCommand):

    def handle(self, *args, **options):
        LoadCards().process()
