from django.urls import path
from .views import event, event_list
urlpatterns = [
    path('month/', event, name='month'),              # /event/month/?month=7
    path('events/', event_list, name='event_list'),   # /event/events/?month=March
]