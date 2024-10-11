from django.shortcuts import render
from django.http import HttpResponse
from procureinsight.utils import datastore


def index(request):
    return render(request, "index.html")


def companies(request):
    all_companies = [
        {"company_name": "Google", "description": "Google is a search engine, created by Larry Page and Sergey Brin."},
        {"company_name": "Meta", "description": "Social media platform, created by Mark Zuckerberg."},
        {"company_name": "Palantir", "description": "Sell data analysis software to governments and corporations."},
    ]
    
    return render(request, 'companies.html', {'all_companies': all_companies})


def company(request, company_name):
    """
    Example url: procure.guru/company/google/
    """

    if datastore.isUnsafePattern(company_name):
        return render(request, 'error404.html')

    company_data = datastore.getCompanyDataDummy(company_name)
    if company_data is None:
        return render(request, 'error404.html')
    

    context = {'company_name': company_name, 'company_data': company_data}

    return render(request, 'company.html', context)


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
