from django.views.generic import ListView
from django.shortcuts import render

from cards.models import Card, SETS


class CardList(ListView):
    model = Card

    def get_context_data(self, **kwargs):
        context = super(CardList, self).get_context_data(**kwargs)
        set_name = self.request.GET.get('set', '')
        cards = Card.objects.filter(set_name=set_name)
        max_count = 0
        total = 0
        for card in cards:
            total += card.count
            if card.elite:
                max_count += 1
            else:
                max_count += 2

        context['card_list'] = cards
        context['set_name'] = set_name
        context['sets'] = SETS
        context['owned'] = cards.filter(count__gt=0)
        if cards.count():
            owned_percentage = (context['owned'].count() * 100.0) / cards.count()
        else:
            owned_percentage = 0
        context['owned_percentage'] = '{0:.2f}'.format(owned_percentage)
        context['total'] = total
        if max_count:
            total_percentage = (total * 100.0) / max_count
        else:
            total_percentage = 0
        context['total_percentage'] = '{0:.2f}'.format(total_percentage)
        return context
