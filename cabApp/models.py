from django.db import models
from django.db.models import Model
from django.db.models.fields import CharField

# Create your models here.
class Oneway(models.Model):
    Name = models.CharField(max_length=200)
    Mo_No = models.IntegerField()
    FromCity = models.CharField(max_length=200)
    Tocity = models.CharField(max_length=200)
    date = models.DateField()
    StartTime = models.TimeField()
    CabChoice = models.CharField(max_length=200)
    
    
class RoundTrip(models.Model):
    name = models.CharField(max_length=200)
    mo_No = models.IntegerField()
    fromCity = models.CharField(max_length=200)
    toCity = models.CharField(max_length = 200)
    dateOfJourney = models.DateField()
    dateOfReturn = models.DateField()
    startTime = models.TimeField()
    cabChoice = models.CharField(max_length=200)

class Cabs(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="pics")  

class Packages(models.Model):
    PackageName = models.CharField(max_length=200)
    Price = models.IntegerField()
    CabType = models.CharField(max_length=200)
