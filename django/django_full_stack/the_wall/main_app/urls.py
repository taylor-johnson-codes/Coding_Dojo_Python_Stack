from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('post_message', views.post_message),
    path('login_reg', views.login_reg),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
]