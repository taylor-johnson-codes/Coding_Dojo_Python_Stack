from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def wall(request):
    return render(request, 'wall.html')

def post_message(request):
    return redirect('/')





def login_reg(request):
    return render(request, 'login_reg.html')

def register(request):
    errors = User.objects.validate_registration(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash
        new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)
        request.session['user_id'] = new_user.id  # to automatically login for the user instead of having them login on login page
        return redirect('/success')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user_list = User.objects.filter(email=email)
    if len(user_list) > 0:
        logged_user = user_list[0]
        if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/success')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('/')
    else:
        messages.error(request, "Email doesn't exist in the database. Try again or register.")
        return redirect('/')

def success(request):
    if not "user_id" in request.session:
        messages.error(request, "You must be logged in to see the success page.")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user
        }
        return render(request, 'success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')