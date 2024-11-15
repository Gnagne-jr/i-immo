from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CustomUser)
class AdminUser(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
