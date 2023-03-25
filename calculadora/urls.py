from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sumar/<int:x>/<int:y>/',views.sumar, name='sumar'),
    path('restar/<int:x>/<int:y>/',views.restar, name='restar'),
    path('multiplicar/<int:x>/<int:y>/',views.multiplicar, name='multiplicar'),
]