from __future__ import unicode_literals

from django.db import models

# Create your models here.

class list_of_items(models.Model):
    title=models.CharField(max_length=33)
    def __str__(self):
        return self.title
