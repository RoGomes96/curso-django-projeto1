from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("Home Test")


def sobre(request):
    return HttpResponse("sobre Test")


def contato(request):
    return HttpResponse("contato Test")
