from django.shortcuts import render
from django.http import HttpResponse
from  . models import Student
# Create your views here.


def home(request):
    return (render(request, "home.html")
            )

def about(request):
    return render(request, "about.html")


def contact(request):
    return (render(request, "contact.html")
            )

def services(request):
    return (render(request, "services.html")
            )

def students(request):
    student = Student.objects.all()
    return render(request, 'students.html', {"pupil":Student })