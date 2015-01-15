from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    deptt = models.CharField(max_length=250)
    # mId = models.CharField(max_length=10)

# class Messages(models.Model):