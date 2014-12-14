import django

django.setup()

from cards.models import Card

Card.load()
