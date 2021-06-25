from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)

class Book(models.Model):
    title = models.CharField(max_length=30)
