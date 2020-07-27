from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name needs to be at least 2 characters."
        elif postData['first_name'].isalpha() == False:
            errors['first_name_alpha'] = "First name needs to be letters only."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name needs to be at least 2 characters."
        elif postData['last_name'].isalpha() == False:
            errors['last_name_alpha'] = "Last name needs to be letters only."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format."
        elif User.objects.filter(email = postData['email']):
            errors['email_exists'] = "Email already exists in database."
        if len(postData['password']) < 8:
            errors['password'] = "Password needs to be at least 8 characters."
        if postData['password'] != postData['confirm_password']:
            errors['confirm'] = "Password and Confirm PW don't match."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    # books_uploaded = a list of books uploaded by a given user
    # liked_books = a list of books a given user likes
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class BookManager(models.Manager):
    def validate_book(self, postData):
        errors = {}
        if len(postData['title']) < 1 or len(postData['desc']) < 1:
            errors['empty'] = "All fields are required to be filled out."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)