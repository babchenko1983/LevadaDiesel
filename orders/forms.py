from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email','postal_code','address','delivery',]
        widgets = {'first_name': forms.TextInput(attrs={'class':'form-control',
                                                        'placeholder':'Serhii'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Levada'}),
                   'email': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'slevada@gmail.com'}),
                   'address': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Wolanowska 135/B, Radom, Poland'}),
                   'delivery': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': '"DHL" or "FedEx"....'}),
                   'postal_code': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder':'26-601'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': '+48787364255'}),
                   }


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
