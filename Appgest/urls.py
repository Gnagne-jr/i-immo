from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("login/", login_user, name='login'),
    path("inscription/", register, name="register"),
]
