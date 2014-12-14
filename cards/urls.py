from django.conf.urls import patterns, url

from cards.views import CardList


urlpatterns = patterns('cards.views',
    url(r'^$', CardList.as_view()),
)
