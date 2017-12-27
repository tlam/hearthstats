from django.conf.urls import url

from cards.views import CardList, CollectionView, SetRarityView


app_name = 'cards'
urlpatterns = [
    url(r'^$', CardList.as_view(), name='index'),
    url(r'^(?P<set_code>\w+)$', CardList.as_view(), name='show'),
    url(r'^collection.json$', CollectionView.as_view()),
    url(r'^(?P<set_code>\w+)/set_rarity.json$', SetRarityView.as_view()),
]
