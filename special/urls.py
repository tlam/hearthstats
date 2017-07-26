from django.conf.urls import url

from special.views import SpecialView


urlpatterns = [
    url(r'^autocomplete/$', SpecialView.as_view(), name='autocomplete'),
]
