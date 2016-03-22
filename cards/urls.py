from django.conf.urls import url

from cards.views import CardList, CollectionView, SetRarityView


urlpatterns = [
    url(r'^$', CardList.as_view()),
    url(r'^collection.json$', CollectionView.as_view()),
    url(r'^(?P<set_name>\w+)/set_rarity.json$', SetRarityView.as_view()),
]
