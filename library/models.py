   
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


class Borrowing(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

def check_eligibility(student):
    max_books_allowed = student.max_books_allowed
    current_borrowed = Borrowing.objects.filter(student=student, is_returned=False).count()
    if current_borrowed >= max_books_allowed:
        return False
    return True

