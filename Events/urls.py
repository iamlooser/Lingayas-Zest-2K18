
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.events, name='Events'),
    url(r'^DayTwo/$', views.DayTwo, name='DayTwo'),

]
