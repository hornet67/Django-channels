from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse({
        'message': 'Hello, World!',
        'name': 'John Doe'
    })



