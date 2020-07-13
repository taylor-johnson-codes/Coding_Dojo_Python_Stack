from django.shortcuts import render

def index(request):
    if "count" not in request.session:
        request.session['count'] = 1
        # this creates a key called 'count' inside the session dict with a value of 1
    else:
        request.session['count'] += 1
    return render(request, "index.html")

def destroy(request):
    del request.session['count']
    return render(request, "index.html")