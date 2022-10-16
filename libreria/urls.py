from unicodedata import name

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('login', views.login, name='login'), 
    path('especialistas', views.especialistas, name='especialistas'),
    path('saludmental', views.saludmental, name='saludmental'),
    path('talleres', views.talleres, name='talleres'),
    path('cita', views.cita, name='cita'),
]