from django.db import models

# Create your models here.
class Admin(models.Model):
    location=models.CharField(max_length=120)
    centers=models.CharField(max_length=120)
    slots=models.PositiveIntegerField()
