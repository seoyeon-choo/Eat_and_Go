from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    cust_id = models.IntegerField(null=True)
    name = models.CharField(max_length=128) #아이디
    phone = models.CharField(max_length=128, unique=True)
    nickname = models.CharField(max_length=128, default="덕우") #이름