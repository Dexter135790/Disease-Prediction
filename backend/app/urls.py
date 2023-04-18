from django.urls import path
from .views import index,result,restart_server

urlpatterns = [
    path('', index, name='Home'),
    path('result/',result,name='Results'),
    path('',restart_server,name="Re"),
]