from django.contrib import admin
from .models import Company, Product, ProductPricing

class ProductPricingInline(admin.TabularInline):
    model = ProductPricing
    extra = 1  # Allows the user to add 1 extra inline

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1  # Allows the user to add 1 extra inline
    inlines = [ProductPricingInline]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded_date', 'employees_count')
    search_fields = ('name',)
    inlines = [ProductInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'cost')
    search_fields = ('name',)
    inlines = [ProductPricingInline]
