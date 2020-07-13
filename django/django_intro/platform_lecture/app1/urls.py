from django.urls import path     
from . import views     # the . indicates that the views file can be found in the same directory as this file

urlpatterns = [
    path('', views.index),  
    # 2 args: 
    # 1) '' - the rest of the route both starts and ends with nothing (i.e. "/" is the full route)
    # 2) views.index - if the requested route matches this pattern, then the function with the name "index" from this app's views.py file will be invoked
    
    # path('bears', views.one_method),                        # would only match localhost:8000/bears
    # path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
    # path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
    # path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown

    path('another_route', views.another_method),
    
    path('redirected_route', views.redirected_method),

    path('HTMLexample', views.HTMLexample),

    path('HTML_py_input', views.HTML_py_input),

    path('users/<int:num>', views.users),

    # path('process_card', views.process),


]