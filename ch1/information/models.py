from django.db import models


class Information(models.Model):
    name = models.CharField(max_length=50)
    fullName = models.CharField(max_length=100)
    CEO = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    Email = models.EmailField()
    Tel = models.CharField(max_length=30)
    bank = models.CharField(max_length=50)
    event = models.TextField()
    businessLicense = models.CharField(max_length=50)
    businessHours = models.CharField(max_length=100)
    roomNum = models.IntegerField()
    logo = models.ImageField(upload_to='information/')
    image1 = models.ImageField(upload_to='information/')
    image2 = models.ImageField(upload_to='information/')
    image3 = models.ImageField(upload_to='information/')
    image4 = models.ImageField(upload_to='information/')