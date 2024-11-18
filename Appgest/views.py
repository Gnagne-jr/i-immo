from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import *

User = get_user_model()

def index(request):
    return render(request, 'index.html')

def gest_bien(request):
    return render(request, 'GestionBiens.html')

@login_required
def dashboard(request):
   
    commune = request.user.commune
    utilisateurs = CustomUser.objects.filter(commune=commune, is_contribuable=True)
    biens = BienImobilier.objects.filter(commune=commune)

    context = {
        'commune': commune,
        'utilisateurs': utilisateurs,
        'biens': biens,
    }

    return render(request, 'dashboard.html', context)


def login_user(request):
    """
     fonction de connexion
    """

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Identifiant ou mot de passe incorrect")
            return redirect('login')
    
    return render(request, "connexion.html")


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)

            user.password = make_password(form.cleaned_data['password'])
        
            user.save()

            return redirect('index')
        else:
            print("Le formulaire n'est pas valide")
    else:
        form = UserForm()

    return render(request, 'inscription.html', {'form': form})



def declare_bien(request):
    if request.method == 'POST':
        form = DeclarationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            return redirect('index')  # Redirige après la soumission
    else:
        form = DeclarationForm()

    return render(request, 'declare_bien.html', {'form': form})


    