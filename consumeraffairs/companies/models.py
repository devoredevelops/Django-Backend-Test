from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(name='Compnay name', max_length=64)
