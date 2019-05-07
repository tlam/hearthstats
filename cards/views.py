from django.http import JsonResponse
from django.views.generic import TemplateView

from cards.models import Card
from expansions.models import Expansion


class CardList(TemplateView):
    model = Card
    template_name = 'cards/card_list.html'

    def get_context_data(self, **kwargs):
        rarity = self.request.GET.get('rarity', '')
        context = super(CardList, self).get_context_data(**kwargs)
        set_code = kwargs.get('set_code', '')
        expansions = Expansion.objects.all()

        try:
            expansion = Expansion.objects.get(code=set_code)
            stats = Card.grand_total(expansion.name)
            if rarity:
                cards = Card.objects.filter(set_name=expansion.name, rarity=rarity)
            else:
                cards = Card.objects.filter(set_name=expansion.name)
        except Expansion.DoesNotExist:
            stats = Card.grand_total('')
            cards = Card.objects.all()

        context['card_list'] = cards
        max_count = stats['total']
        distinct_total = stats['distinct_total']
        context['distinct_total'] = distinct_total
        context['max_count'] = max_count
        total_owned = stats['total_owned']
        context['set_code'] = set_code
        context['expansions'] = expansions
        context['owned'] = cards.filter(count__gt=0)
        if distinct_total:
            owned_percentage = (context['owned'].count() * 100.0) / distinct_total
        else:
            owned_percentage = 0
        context['owned_diff'] = distinct_total - context['owned'].count()
        context['total_diff'] = max_count - total_owned
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
        set_code = context['set_code']
        try:
            expansion = Expansion.objects.get(code=set_code)
            data = Card.grand_total(expansion.name)
        except Expansion.DoesNotExist:
            data = []
        return JsonResponse(data, safe=False)
