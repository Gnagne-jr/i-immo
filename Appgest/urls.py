from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name='index'),
    path("login/", login_user, name='login'),
    path('deconnexion/', deconexion, name='deconexion'),
    path("inscription/", register, name="register"),
    path('contact/', contact, name='contact'),
    path('gestion-de-bien-immobilier/', gest_bien, name='gest_bien'),
    path('declaration-de-bien/', declare_bien, name='declare_bien'),
    path('tableau-de-bord-agent/', dashboard, name='dashboard'),
    path('dashboard/contribuable/', contribuable_dashboard, name='contribuable_dashboard'),
    path('mettre_a_jour_bien/<int:bien_id>/', mettre_a_jour_bien, name='mettre_a_jour_bien'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
