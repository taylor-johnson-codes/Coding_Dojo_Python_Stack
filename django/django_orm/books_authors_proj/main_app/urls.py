from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_book', views.create_book),
    path('create_author', views.create_author),
    path('addAuthorToBook', views.addAuthorToBook), # needed when sending back info thru post method to create a relationship
    path('books/<int:book_id>', views.show_book),
    path('authors/<int:author_id>', views.show_author),
]