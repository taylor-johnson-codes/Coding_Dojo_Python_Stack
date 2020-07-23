from django.db import models

class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        if len(postData['first_name']) or len(postData['last_name']) or len(postData['email']) or len(postData['password']) < 1:
            errors['empty'] = "All fields are required to be filled out."
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
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.password}'

class BookManager(models.Manager):
    def validate_book(self, postData):
        errors = {}
        if len(postData['title']) or len(postData['desc']) < 1:
            errors['empty'] = "All fields are required to be filled out."
        return errors
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded") # OneToMany
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.title} {self.desc} {self.uploaded_by} {self.users_who_like}'