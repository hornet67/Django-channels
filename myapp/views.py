from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.



def chat_view(request):
    return render(request, 'index.html')
        


