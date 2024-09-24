from django.db import models

from django.contrib.auth.models import AbstractUser

class Game(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()

class User(AbstractUser):
    login_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)

class Tag(models.Model):
    name = models.CharField(max_length=20)




