from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá Mundo! Esta é a página inicial do aplicativo.")

# Create your views here.

def sobre(request):
    return HttpResponse("Esta é a página sobre do meu site")