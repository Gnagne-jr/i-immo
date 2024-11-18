from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CustomUser)
class AdminUser(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
@admin.register(BienImobilier)
class AdminBienImmob(admin.ModelAdmin):
    list_display = ['user','type_bien', 'adresse', 'photo1', 'photo3', 'photo4']
