from django.db import models
    
class Movie(models.Model):
    # id field is implicitly created
    # columns in database:
    title = models.CharField(max_length=45)  # CharField requires max_length parameter
    description = models.TextField()
    release_date = models.DateTimeField()
    good_movie = models.BooleanField()
    duration = models.IntegerField()
    movie_in_minutes = models.FloatField()  # good for numbers with potentially varying numbers of decimal places
    ticket_price = models.DecimalField(max_digits=4, decimal_places=2)  # good a number with a fixed number of decimal places, like currency; 
    # 2 required parameters: max_digits refers to the total number of digits (before and after the decimal place), 
    # and decimal_places refers to how many decimal places.
    created_at = models.DateTimeField(auto_now_add=True)  # optional paramenter; adds the current date/time when an object is created
    updated_at = models.DateTimeField(auto_now=True)  # optional paramenter; automatically updates any time the object is modified

# Now run "python manage.py makemigrations" then "python manage.py migrate" in terminal***

    # to override models __str__ method:
    def __repr__(self):
        return "Title: {}".format(self.title)
    # or
    def __str__(self):
        return f"<Movie object: {self.title} ({self.id})>"


# To interact with the database in the terminal shell with ORM commands:
# run "python manage.py shell"
# run "from main_app.models import Movie" and now you can query it; example queries:

# "Movie.objects.all()" - queries for every Movie instance/record/row

# "Movie.objects.create(title="Zoolander", description="comedy", release_date=2001-09-28, good_movie=True  etc.)" - create a new instance
#    When creating: don't have to put in id, created_at or updated_at; those are done automatically

# "Movie.objects.first().__dict__" - to see contents in dictionary form; .first() refers to the first instance/record/row of Movie

# "Movie.objects.first()" will return how you asked it to return in the __repr__(self) method created above

# "Movie.objects.get(id=<enter number>)" - will throw an error unless only and exactly one record matches the query

# "Movie.objects.filter(field1="value for field1", etc.) - gets any records matching the query provided

# "Movie.objects.exclude(field1="value for field1", etc.) - gets any records not matching the query provided

# Updating an existing record:
#    c = ClassName.objects.get(id=1)
#    c.field_name = "some new value for field_name"
#    c.save()

# Deleting an existing record:
#    c = ClassName.objects.get(id=1)
#    c.delete()

# Displaying records:
# ClassName.objects.get(id=1).__dict__ - shows all the values of a single record as a dictionary
# ClassName.objects.all().values() - shows all the values of a QuerySet (i.e. multiple instances)

# Ordering records:
# ClassName.objects.all().order_by("field_name") - orders by field provided, ascending
# ClassName.objects.all().order_by("-field_name") - orders by field provided, descending

# exit() to exit shell

# ***  makemigrations is a kind of staging. When this command runs, Django looks through all our code, finds any changes we made to our 
# models that will affect the database, and then formulates the correct Python code to move on to the next step. Note that if this step has errors, 
# the next step will not work, so you will need to fix any errors before you can move on to migrating.

# migrate actually applies the changes made above. This step is where the SQL queries are actually built and executed.

# optional GUI to view databases: download a program called DB Browser for SQLite (have it closed while you're doing work on your program)
# optional install iPython (pip install ipython); replaces the default shell with a prettier one