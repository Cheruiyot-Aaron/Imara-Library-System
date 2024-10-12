from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    edition = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def total_value(self):
        return self.cost * self.quantity

    def __str__(self):
        return self.title
