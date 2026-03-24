from django.urls import path
from .views import *


urlpatterns = [
        path('', home, name='home'), 
        path('data/', data1, name='data'), 
    ]
