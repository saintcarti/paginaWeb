from django.contrib import admin
from .models import Categoria,Marca,Camara
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['idCategoria', 'nombreCategoria']

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['idMarca', 'nombreMarca']

@admin.register(Camara)
class CamaraAdmin(admin.ModelAdmin):
    list_display = ['idCamara', 'nombreCamara', 'precio', 'descripcion', 'categoria', 'marca']