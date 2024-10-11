from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def companies(request):
    all_companies = [
        {"company_name": "Google", "description": "Google is a search engine, created by Larry Page and Sergey Brin."},
        {"company_name": "Meta", "description": "Social media platform, created by Mark Zuckerberg."},
        {"company_name": "Palantir", "description": "Sell data analysis software to governments and corporations."},
    ]
    
    return render(request, 'companies.html', {'all_companies': all_companies})


def company(request):

    # Sample data to pass to the template
    products_data = [
        {"product": "Collapzable Card Example 1", "content": "This is the content for card 1."},
        {"product": "Collapsable Card Example 2", "content": "This is the content for card 2."},
        {"product": "Collapsable Card Example 3", "content": "This is the content for card 3."},
        {"product": "Collapsable Card Example 4", "content": "This is the content for card 4."},
    ]

    return render(request, 'company.html', {'products_data': products_data})


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
