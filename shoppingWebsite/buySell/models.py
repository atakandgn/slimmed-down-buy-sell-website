# models.py

from django.db import models
# models.py

from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    count = models.IntegerField()

class Subcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    count = models.IntegerField()
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
