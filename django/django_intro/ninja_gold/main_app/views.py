from django.shortcuts import render, redirect
import random

def index(request):
    request.session['coins'] = 0
    # this creates a key called 'coins' inside the session dict with a value of 1
    return render(request, "index.html")

def process(request):
    if request.POST['hidden_process'] == 'farm':
        request.session['coins'] += random.randint(10,20)
    elif request.POST['hidden_process'] == 'cave':
        request.session['coins'] += random.randint(5,10)
    elif request.POST['hidden_process'] == 'house':
        request.session['coins'] += random.randint(2,5)
    elif request.POST['hidden_process'] == 'casino':
        request.session['coins'] += random.randint(-50,50)
    return render(request, "index.html")

def destroy(request):
    del request.session['coins']
    return redirect('/')