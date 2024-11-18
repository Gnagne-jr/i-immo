from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("login/", login_user, name='login'),
    path("inscription/", register, name="register"),
    path('gestion-de-bien-immobilier/', gest_bien, name='gest_bien'),
    path('declaration-de-bien/', declare_bien, name='declare_bien'),
    path('tableau-de-bord-agent/', dashboard, name='dashboard')
]
