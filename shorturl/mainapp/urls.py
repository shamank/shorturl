from django.urls import path
from .views import Shorturl, homepage, makeurl, history_urls, result_url

urlpatterns = [
    path('', homepage, name='home'),
    path('goto/<slug:s_url>/', Shorturl, name='s_url'),
    path('make/', makeurl, name='make_url'),
    path('history/', history_urls, name='history_urls'),
    path('result/<slug:slug>', result_url, name='result_url')
]