from django.shortcuts import render, redirect
from .models import *

def index(request):
    all_dojos_from_DB = Dojo.objects.all()
    context = {
        "all_dojos" : all_dojos_from_DB
    }
    return render(request, 'index.html', context)

def create_dojo(request):
    new_dojo = Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def create_ninja(request):
    dojo_from_template = Dojo.objects.get(id = request.POST['dojo_id'])
    new_ninja = Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo=dojo_from_template)
    return redirect('/')

def delete_dojo(request, dojo_id):
    dojo_to_delete = Dojo.objects.get(id = dojo_id)
    dojo_to_delete.delete()
    return redirect('/')