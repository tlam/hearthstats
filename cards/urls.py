from django.conf.urls import patterns, url

from cards.views import CardList, CollectionView


urlpatterns = patterns('cards.views',
    url(r'^$', CardList.as_view()),
    url(r'^collection.json$', CollectionView.as_view()),
)
