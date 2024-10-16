# views.py

from django.shortcuts import render
from django.http import HttpResponse
from procureinsight.utils.datastore import Datastore
from procureinsight.utils.dummyDatastore import DummyDatastore

dummy_datastore = DummyDatastore()
datastore = Datastore()

def index(request):
    return render(request, "index.html")


def companies(request):
    """ Example url: procure.guru/companies/ """
    companies = datastore.getAllCompanies()
    
    return render(request, 'companies.html', {'companies': companies})


def company(request, company_name):
    """ Example url: procure.guru/company/google/ """

    company_data = dummy_datastore.getCompany(company_name)
    if company_data is None:
        return render(request, 'error404.html')
    

    context = {
        'company_name': company_name,
        'company_data': company_data
    }

    return render(request, 'company.html', context)


def product(request, company_name, product_name):
    """ Example url: procure.guru/company/atlassian/jira/ """

    product_data = dummy_datastore.getProduct(product_name)
    if product_data is None:
        return render(request, 'error404.html')
    

    context = {
        'company_name': company_name,
        'product_name': product_name,
        'product_data': product_data
    }

    return render(request, 'product.html', context)


def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "dashboard.html")

def tables(request):
    return render(request, "tables.html")

def charts(request):
    return render(request, "charts.html")

def cards(request):
    return render(request, "cards.html")

def error404(request):
    return render(request, "error404.html")
