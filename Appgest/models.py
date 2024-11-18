from django.db import models

from django.contrib.auth.models import AbstractUser, User

class CustomUser(AbstractUser):
    COMMUNE_CHOICES = [
        ('abobo', 'Abobo'),
        ('adjame', 'Adjamé'),
        ('attecoube', 'Attécoubé'),
        ('cocody', 'Cocody'),
        ('koumassi', 'Koumassi'),
        ('plateau', 'Le Plateau'),
        ('port-bouet', 'Port-Bouët'),
        ('san-pedro', 'San-Pédro'),
        ('treichville', 'Treichville'),
        ('yopougon', 'Yopougon'),
        ('batisse', 'Bâtisse'),
        ('anyama', 'Anyama'),
        ('grand-bassam', 'Grand-Bassam'),
        ('dabou', 'Dabou'),
        ('grand-lahou', 'Grand-Lahou'),
        ('agboville', 'Agboville'),
    
    ]
    is_agent = models.BooleanField(default=False)
    is_contribuable = models.BooleanField(default=False)
    commune = models.CharField(choices=COMMUNE_CHOICES, max_length=100)
    # numero = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}"


class BienImobilier(models.Model):
    COMMUNE_CHOICES = [
        ('abobo', 'Abobo'),
        ('adjame', 'Adjamé'),
        ('attecoube', 'Attécoubé'),
        ('cocody', 'Cocody'),
        ('koumassi', 'Koumassi'),
        ('plateau', 'Le Plateau'),
        ('port-bouet', 'Port-Bouët'),
        ('san-pedro', 'San-Pédro'),
        ('treichville', 'Treichville'),
        ('yopougon', 'Yopougon'),
        ('batisse', 'Bâtisse'),
        ('anyama', 'Anyama'),
        ('grand-bassam', 'Grand-Bassam'),
        ('dabou', 'Dabou'),
        ('grand-lahou', 'Grand-Lahou'),
        ('agboville', 'Agboville'),
    
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    type_bien = models.CharField(max_length=100, choices=[
        ('maison', 'Maison'),
        ('appartement', 'Appartement'),
        ('terrain', 'Terrain'),
        ('locatif', 'Locatif'),
    ])
    adresse = models.CharField(max_length=255)
    valeur = models.DecimalField(max_digits=10, decimal_places=2)
    proprietaire = models.CharField(max_length=100)
    date_acquisition = models.DateField()
    nommbre_chambre = models.IntegerField()
    nbr_hectare = models.FloatField()
    commune = models.CharField(
        max_length=100,
        choices=COMMUNE_CHOICES,
        default='abobo',
    )
    photo1 = models.ImageField(upload_to='photo/')
    photo2 = models.ImageField(upload_to='photo/')
    photo3 = models.ImageField(upload_to='photo/')


    def __str__(self):
        return f"{self.type_bien} - {self.adresse}"
