from django.shortcuts import render, redirect
from .models import User

def index(request):
    request.session['fname'] = None
    request.session['lname'] = None
    request.session['email'] = None
    request.session['age'] = None
    all_users_from_DB = User.objects.all()
    context = {
        "all_users":all_users_from_DB
    }
    return render(request, "index.html", context)

def add_user(request):
    postFirstName = request.POST['fname']
    postLastName = request.POST['lname']
    postEmail = request.POST['email']
    postAge = request.POST['age']
    User.objects.create(first_name=postFirstName, last_name=postLastName, email_address=postEmail, age=postAge)
    return redirect("/")