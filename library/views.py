from django.shortcuts import render, redirect
from .models import Book, Student

def home(request):
    return render(request, 'library/home.html')

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        category = request.POST['category']
        cost = request.POST['cost']
        quantity = request.POST['quantity']
        edition = request.POST['edition']
        book = Book(title=title, author=author, category=category, cost=cost, quantity=quantity, edition=edition)
        book.save()
        return redirect('home')
    return render(request, 'library/add_book.html')

def add_student(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        full_name = request.POST['full_name']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        grade = request.POST['grade']
        student = Student(student_id=student_id, full_name=full_name, date_of_birth=date_of_birth,
                          email=email, mobile_number=mobile_number, grade=grade)
        student.save()
        return redirect('home')
    return render(request, 'library/add_student.html')
