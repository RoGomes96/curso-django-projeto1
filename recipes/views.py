from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, "home.html")


def sobre(request):
    return HttpResponse("sobre Test")


def contato(request):
    return HttpResponse("contato Test")
