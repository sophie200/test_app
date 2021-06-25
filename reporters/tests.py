from django.test import TestCase
from django.urls import reverse

from .models import Reporter, Pant, Book
from payment.models import Shirt

class ReporterTests(TestCase):

    def setUp(self):
        self.reporter = Reporter.objects.create(first_name='John',
                                                last_name='Smith',
                                                email='john@example.com')
        #q = Article.objects.filter(headline='Global Warming').filter(pub_date="10-20-20").filter(reporters=self.reporter)
        self.shirt = Shirt.objects.create(color="red")
        # ^ can add size=XL, to show how this parser says delete model but should be remove field
        self.pant = Pant.objects.create(color="red", size="XL")
        self.book = Book.objects.create(color="red", length=5)
    
    def test_reporter(self):
        self.assertEqual(f'{self.reporter.first_name}', 'John')
        self.assertEqual(f'{self.reporter.last_name}', 'Smith')
        self.assertEqual(f'{self.reporter.email}', 'john@example.com')
        self.assertEqual(f'{self.shirt.color}', 'red')
