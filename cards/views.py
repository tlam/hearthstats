from django.http import JsonResponse
from django.views.generic import ListView, TemplateView

from cards.models import Card
from utils import constants


class CardList(ListView):
    model = Card

    def get_context_data(self, **kwargs):
        context = super(CardList, self).get_context_data(**kwargs)
        set_name = self.request.GET.get('set', '')
        cards = Card.objects.filter(set_name=set_name)
        stats = Card.grand_total(set_name)
        max_count = stats['total']
        distinct_total = stats['distinct_total']
        total_owned = stats['total_owned']

        context['card_list'] = cards
        context['distinct_total'] = distinct_total 
        context['max_count'] = max_count
        context['set_code'] = {v: k for k, v in constants.SETS_MAP.items()}.get(set_name, '')
        context['set_name'] = set_name
        context['sets'] = constants.SETS_MAP.values()
        context['owned'] = cards.filter(count__gt=0)
        context['owned_diff'] = distinct_total - context['owned'].count()
        context['total_diff'] = max_count - total_owned
        if cards.count():
            owned_percentage = (context['owned'].count() * 100.0) / distinct_total 
        else:
            owned_percentage = 0
        context['owned_percentage'] = '{0:.2f}'.format(owned_percentage)
        context['rarity'] = stats['rarity']
        context['total_owned'] = total_owned
        if max_count:
            total_percentage = (total_owned * 100.0) / max_count
        else:
            total_percentage = 0
        context['total_percentage'] = '{0:.2f}'.format(total_percentage)
        return context


class CollectionView(TemplateView):

    def render_to_response(self, context, **response_kwargs):
        cards = Card.objects.filter(count__gt=0)
        data = []
        for card in cards:
            data.append({
                'name': card.name,
                'count': card.count,
            })

        return JsonResponse(data, safe=False)


class SetRarityView(TemplateView):

    def render_to_response(self, context, **response_kwargs):
        set_name = context['set_name']
        if set_name in constants.SETS_MAP:
            data = Card.grand_total(constants.SETS_MAP[set_name])
        else:
            data = []
        return JsonResponse(data, safe=False)
