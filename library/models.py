   
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

class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    grade = models.CharField(max_length=50)
    current_loans = models.ManyToManyField(Book, blank=True)
    fines = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.full_name

