from django.db import models

class PaymentMethod(models.Model):
    bank = models.CharField(max_length=100)
    reasoning = models.CharField(max_length=100)

class Shirt(models.Model):
    color = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    