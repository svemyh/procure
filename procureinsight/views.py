from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def tables(request):
    return render(request, 'tables.html')

def datatables(request):
    return render(request, 'datatables.html')

def error404(request):
    return render(request, 'error404.html')