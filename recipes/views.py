from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, "recipes/home.html", status=201, context={
        'Name': 'Rodrigo Gomes'
    })


def sobre(request):
    return render(request, 'temp.html')


def contato(request):
    return HttpResponse("contato Test")
