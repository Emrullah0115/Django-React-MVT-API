from django.db import models

# Create your models here.

class Car(models.Model):
    marka = models.CharField(max_length=20);
    model = models.CharField(max_length=20);
