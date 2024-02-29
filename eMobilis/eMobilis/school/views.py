from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello welcome to eMobilis")
def about(request):
    return HttpResponse("About us ")
def services(request):
    return HttpResponse("we offer website training classes and Android Application Development")
def contact(request):
    return HttpResponse("You can reach us through email;info@gmail.com")


