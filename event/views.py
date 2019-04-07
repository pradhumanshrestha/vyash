from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mass_mail, BadHeaderError
from django.conf import settings
from event.models import *
# from event.forms import EventForm
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def event_view(request):
    title = "Welcome Eventpage."
    page_obj = EventDetail.objects.order_by('-created_at')
    events= paginate_query(request, page_obj, 15)
    context = {
        'title': title,
        'events': events,
    }
    return render(request, 'event/event.html', context)


def event_detail_view(request, event_id):
    title = "Event Detail Page"
    detail = get_object_or_404(EventDetail, pk=event_id)
    context = {
        'title': title,
        'detail': detail,
    }
    return render(request, 'event/eventdetail.html', context)


def paginate_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


