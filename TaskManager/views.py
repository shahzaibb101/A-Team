from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello(request):
    return Response({'message': 'i think i understood this'})

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')