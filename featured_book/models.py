from django.db import models




class featured_book(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_price = models.DecimalField(max_digits=10, decimal_places=2)

# Create your models here.
