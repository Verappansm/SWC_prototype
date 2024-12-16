from django.shortcuts import render
from .models import Event

from django.utils.dateparse import parse_date

def home(request):
    """selected_date = request.GET.get('selected_date')
    if selected_date:
        events = Event.objects.filter(date=selected_date)
    else:
        events = Event.objects.all().order_by('date')  # Order by date
    return render(request, 'event_list/home.html', {'events': events})"""
    events = Event.objects.all()
    dates = [event.date for event in events]
    dates = list(set([date.strftime("%Y-%m-%d") for date in dates]))
    dates.sort()
    if request.GET.get('selected_date'):
        selected_date = request.GET.get('selected_date')
        events = events.filter(date=selected_date)
    return render(request, 'event_list/home.html', {'events': events, 'dates': dates})