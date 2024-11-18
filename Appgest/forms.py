from django.forms import ModelForm
from django import forms
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'commune', 'password']


class DeclarationForm(ModelForm):
    class Meta:
        model = BienImobilier
        fields = '__all__'

        def clean_valeur(self):
            valeur = self.cleaned_data.get('valeur')
            if valeur <= 0:
                raise forms.ValidationError("La valeur doit être supérieure à zéro.")
            return valeur