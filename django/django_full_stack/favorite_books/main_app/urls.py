from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('books', views.books),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.book_id_page),
    path('books/edit_book/<int:book_id>', views.edit_book),
    path('destroy/<int:book_id>', views.destroy),
    path('logout', views.logout),
]