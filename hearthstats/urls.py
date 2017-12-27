from django.conf.urls import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    # Examples:
    # url(r'^$', 'hearthstats.views.home', name='home'),
    path(r'cards/', include('cards.urls', namespace='cards'), name='cards'),
    path(r'utils/', include('utils.urls', namespace='utils'), name='utils'),
    path('admin/', admin.site.urls),
]
