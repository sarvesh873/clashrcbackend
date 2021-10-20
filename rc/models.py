from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
         
        ("Male","Male"),("Female","Female"),("Other","Other")
    
    )
# Create your models here.
class extendeduser(models.Model):
  email = models.EmailField(max_length=200,null=True,default="")
  firstname = models.CharField(max_length=200,null=True,default="")
  lstname = models.CharField(max_length=200,null=True,default="")
  number = models.CharField(max_length=20,null=True,default="")
  gender = models.CharField(max_length=20, choices=GENDER_CHOICES,null=True,default="")
  user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
  