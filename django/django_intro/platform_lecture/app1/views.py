from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def index(request):
    return HttpResponse("This is the equivalent of @app.route('/') in Flask!")

# def one_method(request):                # no values passed via URL
#     pass
    
# def another_method(request, my_val):	# my_val would be a number from the URL
#     pass                                # given the example above, my_val would be 23
    
# def yet_another(request, name):         # name would be a string from the URL
#     pass                                # given the example above, name would be 'pooh'
    
# def one_more(request, id, color): 	    # id would be a number, and color a string from the URL
#     pass                                # given the example above, id would be 17 and color would be 'brown'

def root_method(request):
    return HttpResponse("String response from root_method")

def another_method(request):
    return redirect("/redirected_route")

def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})

def HTMLexample(request):
    return render(request, "index.html")

def HTML_py_input(request):
    context = {                 # context is a variable word, but convension is to call it context
        'first_name':'Taylor',  # hard-coded data for now until we learn the database side
        'last_name':'Johnson',
        'address':{
            'zip':12345,
            'state':'WA'
        },
        "interests" : [
            {'name':'Walking the dog', 'frequency':'every day'},
            {'name':'Watching TV', 'frequency':'every other day'},
            {'name':'Sleeping', 'frequency':'every night'}
        ]
    }
    return render(request, 'index.html', context)  # can only send over one input arg (i.e. one dict with all my data)

def users(request, num):
    return HttpResponse(f"Your user ID is: {num}")

# def process(request):
#     # DO LOGIC FOR CHARGING CARD
#     if successful:
#         return redirect("/success")
#     else:
#         return redirect("/fail")  # or back to checkout page to try again

# def some_function(request):
#     if request.method == "GET":
#         print(request.GET)
#     if request.method == "POST":
#         print(request.POST)

def some_function(request):
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]