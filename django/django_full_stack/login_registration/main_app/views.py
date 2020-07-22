from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')