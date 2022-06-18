from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class SuperHeroes(models.Model):
    name= models.CharField(max_length=50)
    desc=models.TextField()
    image=models.CharField(max_length=400)


    def  __str__(self):
        return self.name