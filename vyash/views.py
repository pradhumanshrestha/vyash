from django.shortcuts import render, redirect, get_object_or_404
from event.models import *


def home_view(request):
    events = EventDetail.objects.all()[:3]
    context = {
        'title':"Homepage",
        'events':events
    }
    return render(request, 'home.html', context)