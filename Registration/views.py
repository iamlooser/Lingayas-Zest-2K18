from django.shortcuts import render, redirect
from Registration.form import RegistrationForm
from django.views.generic import TemplateView, ListView
from Registration.models import Registration_Info
from Registration.form import RegistrationForm

from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    login(request)
def Registration(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Registration/completed')
    form = RegistrationForm()
    return render(request, 'Registration/Registration.html', {'form':form})


def completed(request):
    return render(request, 'index.html')


@login_required
def info(request):
    data = Registration_Info.objects.all()
    return render(request, 'Registration/RegistrationInfo.html', {'data':data})
