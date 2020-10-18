from django.db import models

# Create your models here.
class Registerform_model(models.Model):
    username=models.CharField(max_length=250 ,blank=True)
    Email=models.CharField(max_length=250,blank=True)
    password = models.CharField(max_length=250,blank=True)
    Address=models.CharField(max_length=250,blank=True)
    Mobilenumber=models.CharField(max_length=250,blank=True)
class Image(models.Model):
    user_id = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to = 'images/')
class Contact(models.Model):
    yourname=models.CharField(max_length=255, blank=True)
    emailAdress=models.CharField(max_length=255, blank=True)
    projectdetails=models.CharField(max_length=255, blank=True)