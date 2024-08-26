from django import forms
from .models import Product, Aggregate


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "imagen"]


class AggregateForm(forms.ModelForm):
    class Meta:
        model = Aggregate
        fields = ["name", "price"]
