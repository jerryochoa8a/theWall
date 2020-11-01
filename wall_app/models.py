from django.db import models
from django.contrib.auth.models import UserManager
import re


class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors ={}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        
        if len(post_data['fname']) < 2:
            errors['fname'] = "First Name must be at least 2 characters"

        if len(post_data['lname']) < 2:
            errors['lname'] = "Last Name must be at least 2 characters"

        if len(post_data['password']) < 8:
            errors['pasword'] = "Password has to be a minimum of 8 characters"

        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=60)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    message = models.TextField(max_length=150)
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField(max_length=150)
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    Message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()