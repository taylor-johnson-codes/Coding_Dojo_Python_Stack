from django.urls import path
from . import views

urlpatterns = [
    path('', views.success),  # path('', views.index),  path('', views.wall)
    path('success', views.success),
    path('wall', views.wall),  # path('wall', views.success),
    path('create_message', views.create_message),
    path('create_comment', views.create_comment),
    path('login_reg', views.login_reg),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
]