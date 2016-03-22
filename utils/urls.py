from django.conf.urls import patterns, url

from utils.views import index


urlpatterns = patterns('utils.views',
    url(r'^$', index, name='index'),
)
