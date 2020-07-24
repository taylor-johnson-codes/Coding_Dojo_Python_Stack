from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager): 
    def validate_registration(self, postData):
        errors = {}
        if len(postData['first_name']) < 2: # need letters only
            errors['first_name'] = "First name needs to be at least 2 characters."
        elif postData['first_name'].isalpha() == False:  # OR if not postData['first_name'].isalpha():
            errors['first_name_alpha'] = "First name needs to be letters only."
        if len(postData['last_name']) < 2: # need letters only
            errors['last_name'] = "Last name needs to be at least 2 characters."
        elif postData['last_name'].isalpha() == False:
            errors['last_name_alpha'] = "Last name needs to be letters only."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format."
        # if len(postData['email']) < 1:
            # errors['email'] = "Email is required."
        elif User.objects.filter(email = postData['email']):
            errors['email_exists'] = "Email already exists in database."
        if len(postData['password']) < 8:
            errors['password'] = "Password needs to be at least 8 characters."
        if postData['password'] != postData['confirm_password']:
            errors['confirm'] = "Password and Confirm PW don't match."
        return errors

class MessageManager(models.Manager): 
    def validate_message(self, postData):
        errors = {}
        return errors

class CommentManager(models.Manager): 
    def validate_comment(self, postData):
        errors = {}
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    # messages_posted = list of all messages posted by user
    # comments_posted = list of all comments posted by user
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    text = models.CharField(max_length=255)  # want to avoid same names when chaining i.e. Message.message
    creator =  models.ForeignKey(User, related_name="messages_posted", on_delete=models.CASCADE)  # OneToMany
    # reply_list = list of all comments/replies the message has
    objects = MessageManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    text = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="comments_posted", on_delete=models.CASCADE) # OneToMany
    reply =  models.ForeignKey(Message, related_name="reply_list", on_delete=models.CASCADE) # OneToMany
    objects = CommentManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
