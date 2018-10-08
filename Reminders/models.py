from django.db import models

# Create your models here.
class Reminders(models.Model):
    reminderID = models.AutoField(primary_key=True)
    reminderTitle = models.CharField(max_length=50)
    reminderDetails = models.CharField(max_length=200)
    reminderDate = models.DateField()
    reminderTime = models.TimeField()
    reminderPriority = models.CharField(max_length=6)