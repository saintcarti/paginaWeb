from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'iniciotemplates/index.html')


def contacto(request):
    return render(request,'iniciotemplates/indexnosotros.html')

def galery(request):
    return render(request,'iniciotemplates/indexPlanes.html')


def base(request):
    return render(request,'base.html')