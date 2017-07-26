# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from dal import autocomplete
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from cards.models import Card


class SpecialView(View):

    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            cards = Card.objects.filter(name__icontains=query)
        else:
			cards = Card.objects.order_by('name')
        data = {'pagination': {'more': False}, 'results': []}
        for card in cards:
            data['results'].append({
                'id': '{}'.format(card.id),
                'text': card.name
            })
        return JsonResponse(data, safe=False)
