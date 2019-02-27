from django.db import models
from django.urls import reverse


class Company(models.Model):
    """ The Company model """
    name = models.CharField(
        name='name', max_length=64, help_text='Company name', unique=True)

    def get_absolute_url(self):
        return reverse('companies:detail', kwargs={'name': self.name})

    def __str__(self):
        return self.name
