from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, 'index.html')



def events(request):
    return render(request, 'events/events.html')


def updatesoon(request):
    return render(request, 'UpdateSoon.html')
