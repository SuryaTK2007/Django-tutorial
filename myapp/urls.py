from django.urls import path
from .views import event, event_list, month_selection
urlpatterns = [
    path('', month_selection, name='month_selection'),  # /event/
    path('month/', event, name='month'),              # /event/month/?month=7
    path('events/', event_list, name='event_list'),   # /event/events/?month=March
]