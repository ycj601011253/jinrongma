from django.db import models

# Create your models here.

class Buyer(models.Model):

    email=models.EmailField()
    password=models.CharField(max_length=32)

class Company(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32)