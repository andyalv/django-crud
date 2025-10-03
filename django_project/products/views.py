from django.shortcuts import render
from .models import Product

def index(request):
    db_products = Product.objects.all()
    return render(request, 'index.html', { "products": db_products })
