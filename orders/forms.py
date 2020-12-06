from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'postal_code', 'address', 'delivery','payment', 'privacy']
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Serhii'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Levada'}),
                   'email': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'levadadieselpl@gmail.com'}),
                   'address': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Wolanowska 135B, 26-601 Radom, Polska'}),
                   # 'delivery': forms.TextInput(attrs={'class': 'form-control',
                   #                                    'placeholder': '"DHL" or "DPD"....'}),
                   'postal_code': forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': '26-601'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': '+48787364255'}),
                   }
