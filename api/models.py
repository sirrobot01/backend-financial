from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

<<<<<<< HEAD
# Create your models here.
=======

class Expense(models.model):
    purchase_date = models.DateTimeField   # I was thinking we should add a date and time for tracking
    item = models.CharField(max_length=255)
    description = model.TextField()
    amount = model.IntegerField()


class Meta:
    ordering = ['created_on']
    
def _unicode_(self):
    return self.item
>>>>>>> b6a4051b6087e31355a35712bb710c9fccf610b7
