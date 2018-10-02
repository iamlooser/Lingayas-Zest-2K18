
from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [


    url(r'^login/$', login, {'template_name': 'Registration/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'index.html'}, name='logout'),




    url(r'^$', views.Registration, name='Registration'),
    url(r'^completed/$', views.completed, name='reg_completed'),
    url(r'^info/$', views.info, name='reg_info'),

]
