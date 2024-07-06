from django.urls import path

from .views import  exit,iniciosesion, recuperar, registro
urlpatterns = [
    path('logout/', exit, name='logout'),
    path('login/', iniciosesion, name='login'),
    path('recuperar/', recuperar, name='recuperar'),
    path('registro/', registro, name='registro'),
]
