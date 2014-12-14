from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hearthstats.views.home', name='home'),
    url(r'^cards/', include('cards.urls', namespace='card'), name='cards'),
    url(r'^admin/', include(admin.site.urls)),
)
