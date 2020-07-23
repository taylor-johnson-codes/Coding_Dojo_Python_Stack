from django.db import models

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
        if len(postData['email']) < 1:
            errors['email'] = "Email is required."
        elif User.objects.filter(email = postData['email']):  # or len() > 0  # Ninja bonus
            errors['email_exists'] = "Email already exists in database."
        if len(postData['password']) < 8:
            errors['password'] = "Password needs to be at least 8 characters."
        if postData['password'] != postData['confirm_password']:
            errors['confirm'] = "Password and Confirm PW don't match."
        return errors

        # copy/paste into validations if not using EmailField() in models and input email in HTML:
        # import re
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors['email'] = "Invalid email format!"

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.password}'