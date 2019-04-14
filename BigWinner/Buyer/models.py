from django.db import models


# Create your models here.

class Buyer(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32)


class Company(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32)


class Person_step1(models.Model):
    name = models.CharField(max_length=32)
    sex = models.CharField(max_length=4)
    province = models.CharField(max_length=8)
    city = models.CharField(max_length=8)
    circle = models.CharField(max_length=8)
    username = models.CharField(max_length=8)
    topDegree = models.CharField(max_length=8)
    workyear = models.CharField(max_length=8)
    tel = models.CharField(max_length=8)
    buyer = models.ForeignKey(Buyer,on_delete=True)
