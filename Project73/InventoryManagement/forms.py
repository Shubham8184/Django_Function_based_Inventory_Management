from django import forms
from .models import Product



class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
#'date','provider','productname','price','qty','amount','stock'
        label={
            'qty':'Quantity',
            'productname':'Name Of Product',
        }
        widgets={
            'provider':forms.TextInput(attrs={'placeholder':'Please enter Product Provider Name....'}),
            'price':forms.TextInput(attrs={'placeholder':'Please enter Product Price....'}),
            'qty':forms.TextInput(attrs={'placeholder':'Please enter Product Quantity....'}),
            'amount':forms.TextInput(attrs={'placeholder':'Please enter Product Amount....'}),
            'stock':forms.TextInput(attrs={'placeholder':'Please enter Product Stock....'}),
            'productname':forms.TextInput(attrs={'placeholder':'Please enter Product Name....'}),
            'date':forms.NumberInput(attrs={'type':'date'})
        }