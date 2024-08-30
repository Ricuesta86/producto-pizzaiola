from django import forms
from .models import Product, Aggregate


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "imagen"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter el nombre del producto'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter la descripción del producto'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter el precio del producto'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class AggregateForm(forms.ModelForm):
    class Meta:
        model = Aggregate
        fields = ["name", "price"]
