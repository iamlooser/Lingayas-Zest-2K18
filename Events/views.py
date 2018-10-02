from django.shortcuts import render

# Create your views here.
def events(request):
    return render(request, 'events/Events.html');


def DayTwo(request):
    return render(request, 'events/EventDay2.html');
