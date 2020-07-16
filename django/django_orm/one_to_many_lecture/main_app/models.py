from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # books = a list of books associated with a given author

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE) # notes below
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # on_delete is required

    # related_name='books' is for getting all the books by the author IN THE SHELL:
    # python manage.py shell
    # from main_app.models import Author, Book (now you can query Author and Book)
    # new_author = Author.objects.create(name=Taylor Johnson)
    # new_author.name (returns Taylor Johnson)
    # new_book = Book.objects.create(title='The Coding Dojo Student', author = new_author)
    # new_book.title
    # new_book.author.name
    # another_book = Book.objects.create(title='Life After Coding Dojo', author = new_author)
    # another_book.author.name
    # new_author.books.all() - gives us access to all books/THIS IS 'BOOKS' FROM FOREIGNKEY!
    # for book in new_author.books.all():
    #   print(book.title)

    # when related_name is passed through the Book class, it automatically creates the
    # attribute in the Author class.  It's invisible to see so it's commented out in the 
    # User class here, but it actually exists behind the scenes.