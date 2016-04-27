from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from utils.load_cards import LoadCards


@login_required
def index(request):
    if request.method == 'POST':
        load_cards = LoadCards()
        cards_created = load_cards.process()
        messages.success(request, '{} cards loaded'.format(cards_created))

    context = {}

    return render(
        request,
        'utils/index.html',
        context,

    )
