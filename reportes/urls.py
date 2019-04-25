from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('reportes/', views.listarReportes),
    path('reportes/post', views.registrar),



]