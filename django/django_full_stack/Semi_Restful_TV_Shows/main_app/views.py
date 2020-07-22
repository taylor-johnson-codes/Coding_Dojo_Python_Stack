from django.shortcuts import render, redirect
from django.contrib import messages  # need this for validations
from .models import *

def root(request):
    return redirect('/shows')

def all_shows(request):
    context = {
        'all_shows' : Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new_show_page(request):
    return render(request, 'shows_new.html')

def create(request):
    #1) validate post data:
    errors = Show.objects.show_validator(request.POST)  # request.POST checks entire dict
    # check if the errors dict contains any key/value pairs:
    if len(errors) > 0:
        # loop through each pair and make a flash message:
        for key, value in errors.items():
            messages.error(request, value)  # messages was imported at the top
        return redirect('/shows/new')  # send user back to view to correct errors
    #2) if validation passes, continue on:
    else:
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        desc = request.POST['desc']
        new_show = Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
        return redirect('/shows/' + str(new_show.id))

def shows_info(request, show_id):
    context={
        'show' : Show.objects.get(id=show_id)
    }
    return render(request, 'shows_info.html', context)

def edit(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request, 'shows_edit.html', context)

def update(request, show_id):
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/' + str(show_id) + '/edit')
    else:
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