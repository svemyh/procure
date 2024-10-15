from django.shortcuts import render
from django.http import HttpResponse
from procureinsight.utils import datastore


def index(request):
    return render(request, "index.html")


def companies(request):
    companies = datastore.getAllCompanies()
    print(f'Companies: {companies}')
    return render(request, 'companies.html', {'companies': companies})


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


def product(request, company_name, product_name):
    """
    Example url: procure.guru/company/atlassian/jira/
    """

    if datastore.isUnsafePattern(company_name) or datastore.isUnsafePattern(product_name):
        return render(request, 'error404.html')

    product_data = datastore.get_product_data_dummy(product_name)
    if product_data is None:
        return render(request, 'error404.html')
    

    context = {'company_name': company_name,'product_name': product_name, 'product_data': product_data}

    return render(request, 'product.html', context)


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
