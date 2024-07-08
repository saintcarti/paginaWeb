from django.shortcuts import render
from inventario.models import Camara

# Create your views here.
def inicio(request):
    return render(request,'iniciotemplates/index.html')


def contacto(request):
    return render(request,'iniciotemplates/indexnosotros.html')

def galery(request):
    camaras = Camara.objects.all()
    return render(request,'iniciotemplates/indexPlanes.html',{'camaras':camaras})


def base(request):
    return render(request,'base.html')