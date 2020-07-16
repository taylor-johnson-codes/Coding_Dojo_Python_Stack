from django.shortcuts import render, HttpResponse
from .models import Author, Book

def index(request):
    # To create a record that has this foreign key relationship, 
    # we first need to have an instance of an Author, 
    # and then we can pass it like we have any other field:

	# get an instance of an Author
    this_author = Author.objects.get(id=2)
    # set the retrieved author as the author of a new book
    my_book = Book.objects.create(title="Little Women", author=this_author)
    # or in one line...
    # my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

    # view books with their associated authors:
    some_book = Book.objects.get(id=5)
    some_book.title		# returns a string that is the title of the book
    some_book.author	# returns the Author instance associated with this book
    some_book.author.name	# return the name of the author of this book
    some_book.author.id		# returns the id of the author of this book

    # search based off of a ForeignKey relationship:
    this_author = Author.objects.get(id=2)
    books = Book.objects.filter(author=this_author)
    # one-line version:
    # books = Book.objects.filter(author=Author.objects.get(id=2))

    return HttpResponse("Hello World!")

def some_function(request):
    context = {"authors": Author.objects.all()}		# we're only sending up all the authors
    return render(request, "index.html", context)