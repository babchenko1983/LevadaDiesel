from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email','postal_code','address']

# class CheckoutForm(forms.Form):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': "Ivan"
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': "Ivanov"
#     }))
#     email = forms.EmailField(widget=forms.TextInput(attrs={
#         'placeholder': "youremail@example.com"
#     }))
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': "Tovarys'ka St.64, Zaporizhzhia, Ukraine, 69000"
#     }))
#     phone = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': "+380991234567"
#     }))
