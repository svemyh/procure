from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def tables(request):
    return render(request, "tables.html")


def charts(request):
    return render(request, "charts.html")


def cards(request):
    return render(request, "cards.html")


def error404(request):
    return render(request, "error404.html")
