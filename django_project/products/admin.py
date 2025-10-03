from django.contrib import admin
from .models import Product, ProductCategory

# Register your models here.
admin.site.register([Product, ProductCategory])
