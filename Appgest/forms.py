from django.forms import ModelForm
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'commune', 'password']


class DeclarationForm(ModelForm):
    class Meta:
        model = BienImobilier
        fields = ['type_bien', 'adresse', 'valeur', 'proprietaire', 'date_acquisition', 'nommbre_chambre', 'nbr_hectare', 'commune', 'photo1', 'photo2', 'photo3']

        widgets = {
            'date_acquisition': forms.DateInput(attrs={'type': 'date'}), 
        }

        def clean_valeur(self):
            valeur = self.cleaned_data.get('valeur')
            if valeur <= 0:
                raise forms.ValidationError("La valeur doit être supérieure à zéro.")
            return valeur
        
        def clean_photo1(self):
            photo = self.cleaned_data.get('photo1')
            if photo and len(photo.name) > 100:
                raise ValidationError("Le nom du fichier photo1 dépasse 100 caractères.")
            return photo

        def clean_photo2(self):
            photo = self.cleaned_data.get('photo2')
            if photo and len(photo.name) > 100:
                raise ValidationError("Le nom du fichier photo2 dépasse 100 caractères.")
            return photo

        def clean_photo3(self):
            photo = self.cleaned_data.get('photo3')
            if photo and len(photo.name) > 100:
                raise ValidationError("Le nom du fichier photo3 dépasse 100 caractères.")
            return photo