from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

from rest_framework.viewsets import ModelViewSet
from .serializers import ShortUrlSerializer

from .models import ShortUrls
from .forms import MakeNewUrl

import random, string

import redis
import qrcode
# Create your views here.

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def homepage(request):
    if request.method == 'POST':
        form = MakeNewUrl(request.POST)
        if form.is_valid():
            temp_model = form.save(commit=False)
            if form.cleaned_data['short_url'] == '':
                temp_model.short_url = ''.join(random.sample(string.ascii_letters, random.randint(3, 8)))
            if request.user.is_authenticated:
                temp_model.created_by = request.user
            obj = temp_model
            temp_model.save()
            return redirect(obj)
        else:
            messages.error(request, 'Ошибка! Попробуйте снова!')
    else:
        form = MakeNewUrl()

    return render(request, 'mainapp/index.html', {'form': form})


def makeurl(request):
    if request.method == 'POST':
        form = MakeNewUrl(request.POST)
        if form.is_valid():
            temp_model = form.save(commit=False)
            if form.cleaned_data['short_url'] == '':
                temp_model.short_url = ''.join(random.sample(string.ascii_letters, random.randint(3, 8)))
            if request.user.is_authenticated:
                temp_model.created_by = request.user
            obj = temp_model
            temp_model.save()
            return redirect(obj)
        else:
            messages.error(request, 'Ошибка! Попробуйте снова!')

    else:
        form = MakeNewUrl()

    return render(request, 'mainapp/make_url.html', {'form': form})

def history_urls(request):
    if request.user.is_authenticated:
        data = ShortUrls.objects.filter(created_by=request.user.id).select_related('created_by')
    else:
        data = ''

    return render(request, 'mainapp/history.html', {'urls': data})

#
# below is a variant using
# redis as a method for cache
#     

def cache_history_urls(request):
    if str(request.user.id) in cache:
        data = cache.get(str(request.user.id))
        return render(request, 'mainapp/history.html', {'urls': data})

    else:
        data = ShortUrls.objects.filter(created_by=request.user.id).select_related('created_by')
        result = [dat.to_json() for dat in data]
        cache.set(str(request.user.id), result, timeout=30)
        return render(request, 'mainapp/history.html', {'urls': result})



def info_url(request, slug):
    data = ShortUrls.objects.get(pk=slug)

    return render(request, 'mainapp/info_url.html', {'data': data})

#
# below is a variant using
# redis as a method for cache
#

def cache_info_url(request,slug):
    if slug in cache:
        data = cache.get(slug)
        return render(request, 'mainapp/info_url.html', {'data': data})
    else:
        data = ShortUrls.objects.get(pk=slug)
        result = data.to_json()
        cache.set(slug, result, timeout=CACHE_TTL)
        return render(request, 'mainapp/info_url.html', {'data': result})


def Shorturl(request, s_url):
    model = ShortUrls.objects.get(pk=s_url)
    model.views = model.views + 1
    model.save()
    return redirect(model.full_url)

class ShortView(ModelViewSet):
    queryset = ShortUrls.objects.all()
    serializer_class = ShortUrlSerializer
