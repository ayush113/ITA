from django.db import models

# Create your models here.

class Timings(models.Model):
    placeid = models.AutoField(primary_key=True)
    placeName = models.CharField(max_length=100,unique=True)
    OpenTime = models.TimeField()
    CloseTime = models.TimeField()
    DaysClosed = models.CharField(max_length=20)

