from django.shortcuts import render, redirect
from .models import *

def index(request):
    all_books = Book.objects.all()
    all_authors = Author.objects.all()
    context = {
        "all_books" : all_books,
        "all_authors" : all_authors
    }
    return render(request, 'index.html', context)

def create_book(request):
    new_book = Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def create_author(request):
    new_author = Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/')

def show_book(request, book_id):
    one_book = Book.objects.get(id=book_id)
    all_authors = Author.objects.all()
    context = {
        'book' : one_book,
        "all_authors" : all_authors
    }
    return render(request, 'show_book.html', context)

def show_author(request, author_id):
    if request.method == "GET":
        one_author = Author.objects.get(id=author_id)
        all_books = Book.objects.all()
        context = {
            'author' : one_author,
            'all_books' : all_books
        }
        return render(request, 'show_author.html', context)
    if request.method == "POST":
        book_id = request.POST['book_id']
        book = Book.objects.get(id=book_id)
        author = Author.objects.get(id=author_id)
        # creating relationship:
        book.authors.add(author)  # author.books.add(book)
        return redirect('/authors/' + str(author_id))

def addAuthorToBook(request):
    book_id = request.POST['book_id']
    author_id = request.POST['author_id']
    book = Book.objects.get(id = book_id)
    author = Author.objects.get(id = author_id)
    # creating relationship:
    book.authors.add(author)  # author.books.add(book)
    return redirect('/books/' + str(book_id))