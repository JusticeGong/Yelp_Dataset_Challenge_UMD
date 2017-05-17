from django.db import models

# Create your models here.
from django.db import models


class rec(models.Model):
    uID = models.CharField(max_length=200)
    bID = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)

