from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def login_reg(request):
    return render(request, 'login_reg.html')

def success(request):
    if not "user_id" in request.session:
        messages.error(request, "You must be logged in to see the wall.")
        return redirect('/login_reg')
    else:
        return redirect('/wall')

def register(request):
    errors = User.objects.validate_registration(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login_reg')
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
            return redirect('/login_reg')
    else:
        messages.error(request, "Email doesn't exist in the database. Try again or register.")
        return redirect('/login_reg')

def wall(request):
    if not "user_id" in request.session:
        messages.error(request, "You must be logged in to see the wall.")
        return redirect('/login_reg')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            "all_messages" : Message.objects.all()
        }
        return render(request, 'wall.html', context)

def create_message(request):
    errors = Message.objects.validate_message(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
        user = User.objects.get(id = request.session['user_id'])
        text = request.POST['message']
        Message.objects.create(text = text, creator = user)
        return redirect('/wall')

def create_comment(request):
    errors = Comment.objects.validate_comment(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/wall')
    else:
        text = request.POST['comment']
        creator = User.objects.get(id = request.session['user_id'])
        replying_to = Message.objects.get(id = request.POST['message_id'])
        Comment.objects.create(text=text, creator=creator, replying_to=replying_to)
        return redirect('/wall')

def logout(request):
    request.session.clear()
    return redirect('/')