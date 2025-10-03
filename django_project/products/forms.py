from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'short_description', 'brand',
            'category', 'weight', 'is_featured', 'price', 'cost', 'stock'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'border rounded px-3 py-2 w-full',
                'placeholder': 'Nombre del producto'
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'border rounded px-3 py-2 w-full',
                'placeholder': 'Descripción corta'
            }),
            'description': forms.Textarea(attrs={
                'class': 'border rounded px-3 py-2 w-full',
                'rows': 4,
                'placeholder': 'Descripción detallada'
            }),
            'brand': forms.TextInput(attrs={
                'class': 'border rounded px-3 py-2 w-full',
                'placeholder': 'Marca del producto'
            }),
            'category': forms.Select(attrs={
                'class': 'border rounded px-3 py-2 w-full'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'border rounded px-3 py-2 w-full',
                'min': 0
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 text-green-600 rounded focus:ring-green-500'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'border rounded px-3 py-2 w-full',
                'step': '0.01',
                'min': 0
            }),
            'cost': forms.NumberInput(attrs={
                'class': 'border rounded px-3 py-2 w-full',
                'step': '0.01',
                'min': 0
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'border rounded px-3 py-2 w-full',
                'min': 0
            }),
        }
