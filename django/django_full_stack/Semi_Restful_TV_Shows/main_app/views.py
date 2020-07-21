from django.shortcuts import render, redirect
from .models import *

def root(request):
    return redirect('/shows')

def all_shows(request):
    all_shows = Show.objects.all()
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
    return redirect('/shows/' + str(new_show.id))

def shows_info(request, show_id):
    show = Show.objects.get(id=show_id)
    context={
        'show' : show
    }
    return render(request, 'shows_info.html', context)

def edit(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request, 'shows_edit.html', context)

def update(request, show_id):
    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.desc = request.POST['desc']
    show.save()
    return redirect('/shows/' + str(show_id))
    

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect("/shows")