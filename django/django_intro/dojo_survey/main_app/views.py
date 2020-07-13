from django.shortcuts import render

# this shows the form:
def index(request):
    return render(request, "index.html")

# this processes the form:
def create_user(request):
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_from_form = request.POST['comment']
    context = {
        "name": name_from_form,
        "location": location_from_form,
        "language": language_from_form,
        "comment": comment_from_form
    }
    # this shows the success page:
    return render(request, "result.html", context)