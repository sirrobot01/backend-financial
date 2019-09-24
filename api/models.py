from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Expense(models.model):
    purchase_date = models.DateTimeField   # I was thinking we should add a date and time for tracking
    item = models.CharField(max_length=255)
    description = model.TextField()
    amount = model.IntegerField()


class Meta:
    ordering = ['created_on']
    
def _unicode_(self):
    return self.item
