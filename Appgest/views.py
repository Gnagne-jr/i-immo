from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()

def index(request):
    return render(request, 'index.html')

def gest_bien(request):
    return render(request, 'GestionBiens.html')

def contact(request):
    return render(request, 'contact.html')

def payer_impot(request):
    return render(request, 'Paiementimpot.html')

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

@login_required
def contribuable_dashboard(request):
    if request.user.is_contribuable:
        declarations = BienImobilier.objects.filter(user=request.user)

        context = {
            'declarations': declarations,
        }
        return render(request, 'contribuable_dashboard.html', context)
    else:
        return redirect('unauthorized')


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

def deconexion(request):
    logout(request)
    return redirect("index")


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)

            user.password = make_password(form.cleaned_data['password'])
            user.is_contribuable = True
        
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
        print('okok3')
        if form.is_valid():
            print('okok1')
            declaration = form.save(commit=False)
            declaration.user = request.user
            declaration.save()
            return redirect('index')  
        else:
            print('okoko1')
            print(form.errors)   
    else:
        form = DeclarationForm()

    return render(request, 'declare_bien.html', {'form': form})



def mettre_a_jour_bien(request, bien_id):
    bien = get_object_or_404(BienImobilier, id=bien_id)
    if request.method == 'POST':
        form = BienUpdateForm(request.POST, instance=bien)
        if form.is_valid():
            MAJ = form.save(commit=False)
            MAJ.valeur_due = MAJ.calcul_valeur_due()
            MAJ.save()

            return redirect('dashboard')
    else:
        form = BienUpdateForm(instance=bien)

    return render(request, 'modal_update_form.html', {'form': form, 'bien': bien})
    