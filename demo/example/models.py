from django.db import models

# Create your models here.

class Upload(models.Model):
    filename = models.TextField(blank=True)
