from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    founded_date = models.DateField()
    employees_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    company = models.ForeignKey(Company, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class ProductPricing(models.Model):
    product = models.ForeignKey(Product, related_name='pricing', on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category} - {self.price}"
