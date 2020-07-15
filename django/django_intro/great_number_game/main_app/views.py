from django.shortcuts import render, HttpResponse
import random

def index(request):
    if 'random_num' not in request.session:
        request.session['random_num'] = random.randint(1,100)
    return render(request, "index.html")