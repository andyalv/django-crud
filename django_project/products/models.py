from django.db import models
from djmoney.models.fields import MoneyField

class ProductCategory(models.Model):
    name = models.CharField(max_length=70)

    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Product(models.Model):
    # Basic data
    name = models.CharField(max_length=50)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    brand = models.CharField(max_length=30)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)

    # Price and stock
    price = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency='USD'
    )
    cost = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency='USD',
        blank=True,
        null=True
    )
    stock = models.PositiveIntegerField(default=0)

    # Audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return f"{self.id} - {self.name} [{self.brand}]"

