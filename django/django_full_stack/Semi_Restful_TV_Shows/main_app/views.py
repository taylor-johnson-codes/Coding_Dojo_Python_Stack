from django.shortcuts import render, redirect
from .models import *

def index (request):
    redirect('/shows')

def all_shows_table(request):
    all_shows = Shows.objects.all()
    context = {
        'all_shows' : all_shows
    }
    return render(request, 'shows.html', context)

def new_show_page(request):
    return render(request, 'shows_new.html')

def create(request):
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    desc = request.POST['desc']
    new_show = Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
    all_shows = Shows.objects.all()
    context = {
        'all_shows' : all_shows
    }
    return render(request, 'shows/<int: show_id>', context)

def shows_info(request, show_id):
    show = Show.objects.get(id=show_id)
    context={
        'show' : show
    }
    return render(request, 'shows_info.html', context)

def update(request, show_id):
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    desc = request.POST['desc']
    # edit_show = Show.object.get(id= ???)
    # edit_show MAKE CHANGES
    # edit_show.save
    edit_show = Show.objects.get(id=show_id)
    context = {
        'edit_show' : edit_show
    }
    return render(request, 'shows_info.html', context)

def destroy (request, show_id):
    # destroy CRUD command
    return redirect("/shows")