from django.shortcuts import render
from django.http import HttpResponse

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
    events={
        'January': ['New Year Party', 'Winter Festival'],
        'February': ['Valentine\'s Day', 'Winter Carnival'],
        'March': ['Spring Festival', 'St. Patrick\'s Day'],
        'April': ['Easter', 'Spring Break'],
        'May': ['Labor Day', 'Spring Festival'],
        'June': ['Summer Solstice', 'Graduation'],
        'July': ['Independence Day', 'Summer Festival'],
        'August': ['Summer Vacation', 'Back to School'],
        'September': ['Fall Festival', 'Labor Day'],
        'October': ['Halloween', 'Fall Break'],
        'November': ['Thanksgiving', 'Fall Festival'],
        'December': ['Christmas', 'New Year\'s Eve']
    }
    month = request.GET.get('month')
    if month:
        events_list = events.get(month, [])
        return render(request, 'myapp/event_list.html', {'events': events_list})
    else:
        return HttpResponse("Please provide a month in the query string (e.g., ?month=January) 📅")