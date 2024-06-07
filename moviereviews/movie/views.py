from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('<h2>Witam na stronie głównej</h2>')


def about(request):
    return HttpResponse('<h1>Strona o mnie</h1>')
