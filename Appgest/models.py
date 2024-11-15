from django.db import models

from django.contrib.auth.models import AbstractUser, User

class CustomUser(AbstractUser):
    is_agent = models.BooleanField(name= "est agent", default=False)
    is_contribuable = models.BooleanField(name= "est contribuable", default=False)
    commune = models.CharField(name="Commune", max_length=100)
    # numero = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}"
