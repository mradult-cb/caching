from django.shortcuts import render

from Redis.settings import CACHE_TTL
from .models import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

CACHE_TTL= getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def get_superheros(filter_superheroes = None):
    if filter_superheroes:
        print("===================THIS IS FROM DB======================")
        superheroes=SuperHeroes.objects.filter(name__contains=filter_superheroes)
    else:
        superheroes=SuperHeroes.objects.all()
    return superheroes

def home(request):
    filter_superheroes = request.GET.get('superheroes')
    if cache.get(filter_superheroes):
        print("==========================THIS IS FRM CACHE================")
        superheroes= cache.get(filter_superheroes)
    else:
        if filter_superheroes:
            superheroes=get_superheros(filter_superheroes)
            cache.set(filter_superheroes,superheroes)
        else:
            superheroes=get_superheros()

    context={'superheroes':superheroes}
    return render(request,'home.html', context)

def show(request, id):
    if cache.get(id):
        print("====================THIS DATA IS FROM CACHE===================")
        superheroes=cache.get(id)
    else:
        print("===================THIS DATA IS FROM DB=====================")

        superheroes=SuperHeroes.objects.get(id=id)
        cache.set(id, superheroes)
    context={'superheroes':superheroes}
    return render(request, 'show.html', context)


