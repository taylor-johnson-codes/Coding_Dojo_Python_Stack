from django.db import models

class User(models.Model):
    # id field is implicitly created
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)