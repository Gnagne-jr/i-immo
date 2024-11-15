from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import *

User = get_user_model()

def index(request):
    return render(request, 'index.html')


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
            form.save()
            return redirect('index')
        else:
            print("le formulaire n'est pas correcte")

    else:
        form = UserForm() 

    return render(request, 'inscription.html', {'form':form})       