from django.db import models
    
class User(models.Model):
    # id field is implicitly created
    # columns in database:
    first_name = models.CharField(max_length=50)  # CharField requires max_length parameter
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # optional paramenter; adds the current date/time when an object is created
    updated_at = models.DateTimeField(auto_now=True)  # optional paramenter; automatically updates any time the object is modified

# shell commands ran that were run are in the .txt file in the parent folder