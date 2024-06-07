from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'name': 'Tomek',
                                         'searchTerm': searchTerm})


def about(request):
    return HttpResponse('<h1>Strona o mnie</h1>')
