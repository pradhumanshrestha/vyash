from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_view, name='event' ),
    path('detail/<int:event_id>', views.event_detail_view, name='eventdetail')
]