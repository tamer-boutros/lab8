from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    telephone1 = models.CharField(max_length=100)
    telephone2 = models.CharField(max_length=100)