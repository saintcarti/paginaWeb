from django import forms
from django.forms import widgets
from .models import Camara

class CamaraForm(forms.ModelForm):
    class Meta:
        model = Camara
        fields = ['nombreCamara','precio','marca','categoria','descripcion','imagen','stock']
        labels = {
            'nombreCamara': 'Nombre de camara',
            'precio':'Precio de camara',
            'marca':'Marca de camara',
            'categoria':'Categoria de camara',
            'descripcion':'Descripcion de camara',
            'imagen':'Imagen de camara',
            'stock':'Stock de camara'
        }
        widgets = {
            'nombreCamara': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre de la camara',
                    'id':'nombreCamara'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el precio de la camara',
                    'id':'precio'
                }
            ),
            'marca': forms.Select(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la marca de la camara',
                    'id':'marca'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'categoria'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la descripcion de la camara',
                    'id':'descripcion'
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id':'imagen'
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el stock de la camara',
                    'id':'stock'
                }
            )   
        }