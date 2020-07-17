from django.shortcuts import render, redirect
import random

def index(request):
    request.session['coins'] = 0
    # creates a key called 'coins' in the session dict with a value of 0
    request.session['activity'] = []
    # creates a key called 'activity' in the session dict with a value of an empty array
    request.session.save()  # not required but helps Django not randomly act funny
    return render(request, "index.html")

def process(request):
    place = request.POST['hidden_process']
    if place == 'farm':
        money = random.randint(10,20)
        request.session['coins'] += money
        string = "<div class='gain'>You have earned " + str(money) + " coins from the farm!</div>"
        request.session['activity'].append(string)
    elif place == 'cave':
        money = random.randint(5,10)
        request.session['coins'] += money
        string = "<div class='gain'>You have earned " + str(money) + " coins from the cave!</div>"
        request.session['activity'].append(string)
    elif place == 'house':
        money = random.randint(2,5)
        request.session['coins'] += money
        string = "<div class='gain'>You have earned " + str(money) + " coins from the house!</div>"
        request.session['activity'].append(string)
    elif place == 'casino':
        money = random.randint(-50,50)
        request.session['coins'] += money
        if money >= 0:
            string = "<div class='gain'>You have earned " + str(money) + " coins from the casino!</div>"
            request.session['activity'].append(string)
        elif money < 0:
            string = "<div id='loss'>You have LOST " + str(money*-1) + " coins from the casino.</div>"
            request.session['activity'].append(string)
    request.session.save()  # not required but helps Django not randomly act funny
    return render(request, "index.html")
    # for return redirect('/') to work, I'd need to put 'if coins not in session (etc)' in index function


# not needed because I reset coins/activity to empty when index.html gets reloaded
def destroy(request):
    del request.session['coins']
    return redirect('/')