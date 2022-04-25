from django.db import models
from django.contrib.auth.models import User
from owner.models import Admin

# Create your models here.
class Userprofiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Admin, on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    phone=models.CharField(max_length=12)
    options=(
        ('looking','looking'),
        ('cancelled','cancelled'),
        ('order','order'),
    )
    status=models.CharField(max_length=150,choices=options,default='looking')

