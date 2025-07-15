from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone_number=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    course=models.CharField(max_length=20)
    DOB=models.DateField()
    marks=models.IntegerField()

class Seller(models.Model):
    Sname=models.CharField(max_length=30)
    Saddress=models.CharField(max_length=50)
    Sphno=models.CharField(max_length=10)
    Pname=models.CharField(max_length=20)
    Pcost=models.FloatField()
    