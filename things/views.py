from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from things.models import Thing


def goodbuy(request):
    return HttpResponse('Goodbuy, world! Enjoy the Sails!')


class ThingListView(ListView):
    model = Thing
