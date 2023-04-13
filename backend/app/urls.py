from django.urls import path
from .views import index,result

urlpatterns = [
    path('', index, name='Home'),
    path('result/',result,name='Results'),
]