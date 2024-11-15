from django.forms import ModelForm
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'Commune', 'password']