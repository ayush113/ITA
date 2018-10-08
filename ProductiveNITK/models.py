from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=512)
    email = models.CharField(max_length=200,unique=True)
    userid = models.AutoField(primary_key=True)

