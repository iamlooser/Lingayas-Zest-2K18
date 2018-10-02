
from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('adminoflingayas/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^updatesoon/$', views.updatesoon, name='updatesoon'),
    url(r'^Events/', include('Events.urls')),
    url(r'^Registration/', include('Registration.urls')),

]
