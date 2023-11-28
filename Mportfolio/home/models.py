from django.db import models
from django.utils.timezone import now

# Create your models here.
class Home(models.Model):
    typewrite = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    des = models.CharField(max_length=300)
    img = models.ImageField(upload_to="", default="media/hero.jpeg")

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to="")
    view = models.CharField(max_length=350)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phn = models.CharField(max_length=50)
    msg = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class About(models.Model):
    id = models.AutoField(primary_key=True)
    shortDes = models.CharField(max_length=350)
    experience = models.TextField()
    edu = models.TextField()
    skill = models.TextField()
    achive = models.TextField()

    def __str__(self):
        return self.shortDes
    
    