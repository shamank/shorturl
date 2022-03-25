from django.urls import path
from django.views.decorators.cache import cache_page

from .views import Shorturl, homepage, makeurl, history_urls, info_url

urlpatterns = [
    # path('', cache_page(60)(homepage), name='home'),
    path('', homepage, name='home'),
    path('goto/<slug:s_url>/', Shorturl, name='s_url'),
    path('make/', makeurl, name='make_url'),
    path('history/', history_urls, name='history_urls'),
    path('info/<slug:slug>', info_url, name='info_url')
]