"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from procureinsight import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path(
        "index/", RedirectView.as_view(url="/", permanent=False), name="redirect-home"
    ),
    path("home/", RedirectView.as_view(url="/", permanent=False), name="redirect-home"),
    path("company/<str:company_name>/", views.company, name="company"),
    path("company/<str:company_name>/<str:product_name>/", views.product, name="product"),
    path("companies/", views.companies, name="companies"),
    path("login/", views.login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("tables/", views.tables, name="tables"),
    path("charts/", views.charts, name="charts"),
    path("cards/", views.cards, name="cards"),
    path("error404/", views.error404, name="error404"),
]
