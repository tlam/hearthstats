from django.views.generic import ListView
from django.shortcuts import render

from cards.models import Card, SETS


class CardList(ListView):
    model = Card

    def get_context_data(self, **kwargs):
        context = super(CardList, self).get_context_data(**kwargs)
        set_name = self.request.GET.get('set', '')
        cards = Card.objects.filter(set_name=set_name)
        max_count, total_cards, total = Card.grand_total(set_name)

        context['card_list'] = cards
        context['max_count'] = max_count
        context['set_name'] = set_name
        context['sets'] = SETS
        context['owned'] = cards.filter(count__gt=0)
        context['owned_diff'] = total_cards - context['owned'].count()
        context['total_cards'] = total_cards
        context['total_diff'] = max_count - total
        if cards.count():
            owned_percentage = (context['owned'].count() * 100.0) / total_cards
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
