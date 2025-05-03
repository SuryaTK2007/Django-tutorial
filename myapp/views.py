from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

def home(request):
    return HttpResponse("Hello, world! This is the home page.")

def month_selection(request):
    month = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    
    return render(request, 'myapp/month_selection.html', {'months': month})

def event(request):
    month = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    
    month_str = request.GET.get('month')
    
    if not month_str:
        return HttpResponse("Month parameter is missing 😕")

    try:
        month_number = int(month_str)
    except ValueError:
        return HttpResponse("Month must be a number (e.g., ?month=5) 🚫")

    if month_number < 1 or month_number > 12:
        return HttpResponse("Invalid month number. It must be between 1 and 12 🧭")
    
    month_name = month[month_number - 1]
    return HttpResponse(f"The month is {month_name} 🎉")

# Create your views here.

def event_list(request):
    title = request.GET.get('month')  # This will now be based on 'title', not 'month'
    if title:
        event_doc = Event.objects.filter(title=title).first()
        if event_doc:
            return render(request, 'myapp/event_list.html', {'events': event_doc.event})
        else:
            return HttpResponse(f"No events found for {title} 😶")
    return HttpResponse("Please provide a month (title) in the query string (e.g., ?month=January) 📅")
