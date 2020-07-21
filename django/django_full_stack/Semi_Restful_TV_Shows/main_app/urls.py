from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.all_shows_table),
    path('shows/new', views.new_show_page),
    path('shows/create', views.create),
    path('shows/<int: show_id>', views.shows_info),
    path('shows/<int: show_id>/update', views.update),
    path('shows/<int: show_id>/destroy', views.destroy),
]