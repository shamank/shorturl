from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import ShortUrls
from .forms import MakeNewUrl

import random, string
import qrcode
# Create your views here.


def homepage(request):
    if request.method == 'POST':
        form = MakeNewUrl(request.POST)
        if form.is_valid():
            temp_model = form.save(commit=False)
            if request.user.is_authenticated:
                temp_model.created_by = request.user
            obj = temp_model
            temp_model.save()
            return redirect(obj)
        else:
            messages.error(request, 'Ошибка!')
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
            messages.error(request, 'Ошибка!')

    else:
        form = MakeNewUrl()

    return render(request, 'mainapp/make_url.html', {'form': form})


def history_urls(request):
    if request.user.is_authenticated:
        data = User.objects.get(pk=request.user.id).shorturls_set.all()
    else:
        data = ''

    return render(request, 'mainapp/history.html', {'urls': data})


def result_url(request, slug):
    data = ShortUrls.objects.get(pk=slug)

    return render(request, 'mainapp/result_url.html', {'data': data})


def Shorturl(request, s_url):
    model = ShortUrls.objects.get(pk=s_url)
    return redirect(model.full_url)

