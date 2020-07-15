from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, "index.html")

def add(request):
    postFirstName = request.POST['fname']
    postLastName = request.POST['lname']
    postEmail = request.POST['email']
    postAge = request.POST['age']
    User.objects.create(first_name=postFirstName, last_name=postLastName, email=postEmail, age=postAge)
    return redirect("/")