from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'hearthstats.views.home', name='home'),
    url(r'^cards/', include('cards.urls', namespace='card'), name='cards'),
    url(r'^utils/', include('utils.urls', namespace='utils'), name='utils'),
    url(r'^admin/', include(admin.site.urls)),
]
