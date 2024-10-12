from django.urls import path
from .views import home, add_book, add_student

urlpatterns = [
    path('', home, name='home'),
    path('add_book/', add_book, name='add_book'),
    path('add_student/', add_student, name='add_student'),
]
