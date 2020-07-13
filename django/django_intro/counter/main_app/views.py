from django.shortcuts import render

def index(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    return render(request, "index.html")
    # request.session['name'] = request.POST['name']
    # request.session['counter'] = 100
