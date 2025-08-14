from django.db import models

# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=150)


class Book(models.Model):
    