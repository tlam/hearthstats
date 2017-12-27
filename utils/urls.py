from django.conf.urls import url

from utils.views import index


app_name = 'utils'
urlpatterns = [
    url(r'^$', index, name='index'),
]
