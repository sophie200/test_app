from django.test import TestCase
from django.urls import reverse

from .models import Payment

class ReporterTests(TestCase):

    def setUp(self):
        self.payment = PaymentMethod.objects.create(bank='American',
                                                reasoning='Save')
        self.shirt = Shirt.objects.create(color="red", size="XL", brand="Gap")
    def test_reporter(self):
        self.assertEqual(f'{self.payment.bank}', 'American')
        self.assertEqual(f'{self.payment.reasoning}', 'Save')