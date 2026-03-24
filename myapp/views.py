from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.


def home(request):
    return JsonResponse({
        'message': 'Hello, World!',
        'name': 'John Doe',
        'learning': True
        
    })



def data1(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        return JsonResponse({
            'message': 'Hello, World!',
            'name': 'John Doe',
            'learning': True,
            'name': name,
            'age': age
            
        })
    return JsonResponse({'error': 'Only POST allowed'}, status=400)
        


