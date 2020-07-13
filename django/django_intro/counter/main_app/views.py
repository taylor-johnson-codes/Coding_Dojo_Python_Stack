from django.shortcuts import render, redirect

def index(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = request.POST['num']  # num would come from HTML
    print(request.session['num_visits'])

# checking to see if it's users first time visiting:
# need so app doesn't break
# quickly at recording 1h5m in
    if 'num_visits' in request.session:
        # LOGIC FOR USER ALREADY VISITS
    else:
        # LOGIC FOR USER VISITING FIRST TIME


    if "counter" not in request.session:
        request.session['counter'] = 1

    else:
        request.session['counter'] += 1
    return render(request, "index.html")
    # request.session['name'] = request.POST['name']
    # request.session['counter'] = 100

def destroy(request):
    del request.session['counter']