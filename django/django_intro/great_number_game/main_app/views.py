from django.shortcuts import render, redirect
import random

def index(request):
    if 'random_num' not in request.session:
        request.session['random_num'] = random.randint(1,100)
        request.session['status'] = ''
        return render(request, "index.html")
    if request.session['status'] == 'low':
        return render(request, 'low.html')
    if request.session['status'] == 'high':
        return render(request, 'high.html')
    if request.session['status'] == 'correct':
        return render(request, 'correct.html')
    return render(request, "index.html")

# alternate approach with just using the index.html for all routes:
# use jinja tags and if statements in index.html file

def process(request):
    postGuess = int(request.POST['guess'])  # guess comes back from HTML in string format
    if postGuess == int(request.session['random_num']):
        request.session['status'] = "correct"
    elif postGuess < int(request.session['random_num']):
        request.session['status'] = "low"
    elif postGuess > int(request.session['random_num']):
        request.session['status'] = "high"
    return redirect("/")

def destroy(request):
    # del request.session['random_num']
    # del request.session['status']
    request.session.clear()
    return redirect("/")