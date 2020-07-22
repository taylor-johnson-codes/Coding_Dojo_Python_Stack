from django.db import models

# class with models.Manager inherits from ORM-buildin class and extends models' functionality
class ShowManager(models.Manager):
    # contains all built-in methods plus whatever methods we add here
    def show_validator(self, postData):
        errors = {}
        # adds key/value to errors dict:
        if len(postData['title']) < 2:
            errors['title'] = "Title needs to be at least 2 characters."
        # doesn't work on edit page:
        # if Show.objects.filter(title = postData['title']):
        #     errors['title'] = "Title is already in the database."
        if len(postData['network']) < 3:
            errors['network'] = "Network needs to be at least 3 characters."
        if len(postData['desc']) < 10:
            errors['desc'] = "Description needs to be at least 10 characters."
        return errors

# models.Model makes a database table
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()  # this overrides the original objects property
    def __str__(self):
        return f'{self.title} {self.network} {self.release_date} {self.desc}'