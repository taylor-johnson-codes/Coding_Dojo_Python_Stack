from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
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
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)
        request.session['user_id'] = new_user.id
        return redirect('/books')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user_list = User.objects.filter(email=email)
    if len(user_list) > 0:
        logged_user = user_list[0]
        if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/books')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('/')
    else:
        messages.error(request, "Email doesn't exist in the database. Try again or register.")
        return redirect('/')

def books(request):
    if not "user_id" in request.session:
        messages.error(request, "You must be logged in to see the books.")
        return redirect('/')
    else:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'all_books' : Book.objects.all()
        }
        return render(request, 'books.html', context)

def add_book(request):
    title = request.POST['title']
    desc = request.POST['desc']
    uploaded_by = User.objects.get(id=request.session['user_id'])
    Book.objects.create(title=title, desc=desc, uploaded_by=uploaded_by)
    return redirect('/books')

def book_id_page(request, book_id):
    context={
        'user' : User.objects.get(id=request.session['user_id']),
        'book' : Book.objects.get(id=book_id)
    }
    return render(request, 'book_id_page.html', context)

def edit_book(request, book_id):
    errors = Book.objects.validate_book(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/' + str(book_id))
    else:
        book = Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
        return redirect('/books/' + str(book_id))

def destroy(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/books')

def logout(request):
    request.session.clear()
    return redirect('/')