from django.shortcuts import render,get_object_or_404,redirect
from .models import Camara,Boleta,DetalleBoleta,Categoria,Marca
from .forms import CamaraForm
from .compra import Carrito
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


def admin_required(login_url=None):
    return user_passes_test(lambda u: u.is_active and u.is_staff, login_url=login_url)







# Create your views here.
@login_required
def inventario_view(request):
    camaras = Camara.objects.filter(stock__gt=0)
    context = {
        'camaras':camaras
    }

    return render(request,'vista/Mercado.html',context)

def API(request):
    return render(request,'API/indexAPI.html')
@admin_required()
def listado_camaras(request):
    camaras = Camara.objects.all()
    context = {
        'camaras':camaras
    }
    return render(request,'crud/listado_camaras.html',context)

def detalle_camara(request,id):
    camaraDetalle = Camara.objects.get(idCamara=id)
    
    context= {
        'camara':camaraDetalle
    }

    return render(request,'crud/detalle_camara.html',context)

def editar_camara(request,id):
    camarasModificadas = get_object_or_404(Camara,idCamara= id)
    
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        categoria = get_object_or_404(Categoria, idCategoria=categoria_id)

        marca_id = request.POST.get('marca')
        marca = get_object_or_404(Marca, idMarca=marca_id)

        camarasModificadas.nombreCamara = request.POST.get('nombreCamara')
        camarasModificadas.precio = request.POST.get('precio')
        camarasModificadas.descripcion = request.POST.get('descripcion')
        camarasModificadas.categoria = categoria
        camarasModificadas.marca = marca

        if 'imagen' in request.FILES:
            camarasModificadas.imagen = request.FILES['imagen']

        camarasModificadas.stock = request.POST.get('stock')
        camarasModificadas.save()
    
    categoria = Categoria.objects.all()
    marca = Marca.objects.all()
    context= {
        'camaraModificadas':camarasModificadas,
        'categorias':categoria,
        'marcas':marca
    }
    
    return render(request,'crud/editar_camara.html',context)


def crear_camara(request):
    if request.method == 'POST':
        camaraform = CamaraForm(request.POST,request.FILES)
        if camaraform.is_valid():
            camaraform.save()
            return redirect('listado_camaras')
    else:
        camaraform = CamaraForm()

    return render(request,'crud/crear.html',{'camaraform':camaraform})

def eliminar_camara(request,id):
    camaraEliminada = Camara.objects.get(idCamara=id)
    camaraEliminada.delete()
    return redirect('listado_camaras')

def agregar_producto(request,id):
    carrito_compra = Carrito(request)
    camara = Camara.objects.get(idCamara=id)
    carrito_compra.agregar(camara = camara)
    return redirect('inventario')

def eliminar_producto(request,id):
    carrito_compra = Carrito(request)
    camara = Camara.objects.get(idCamara=id)
    carrito_compra.eliminar(camara = camara)
    return redirect('inventario')

def restar_producto(request,id):
    carrito_compra = Carrito(request)
    camara = Camara.objects.get(idCamara=id)
    carrito_compra.restar(camara = camara)
    return redirect('inventario')

def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('inventario')

def generarBoleta(request):
    camara = Camara.objects.all()

    carrito = request.session.get('carrito', None)
    if not carrito:
        # Redirigir a una página de error o mostrar un mensaje
        return render(request, 'carrito/detallecarrito.html', {'error': 'El carrito está vacío.'})

    precio_total = 0
    productos = []

    for key, value in carrito.items():
        precio_total += int(value['precio']) * int(value['cantidad'])

    # Crear la boleta
    boleta = Boleta(total=precio_total)
    boleta.save()

    # Crear los detalles de la boleta
    for key, value in carrito.items():
        producto = Camara.objects.get(idCamara=value['idCamara'])
        cant = value['cantidad']
        subtotal = cant * int(value['precio'])
        detalle = DetalleBoleta(id_boleta=boleta, id_producto=producto, cantidad=cant, subtotal=subtotal)
        detalle.save()
        productos.append(detalle)

    datos = {
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'total': boleta.total,
        'id_boleta': boleta.id_boleta,
        'camara': camara
    }
    
    request.session['boleta'] = boleta.id_boleta

    # Vaciar el carrito
    carrito = Carrito(request)
    carrito.vaciar()

    return render(request, 'carrito/detallecarrito.html', datos)

def detalleCarrito(request):
    
    carrito = request.session.get('carrito', {})
    carrito_vacio = not bool(carrito)  # True si el carrito está vacío
    return render(request, 'carrito/detallecarrito.html', {'carrito_vacio': carrito_vacio, 'carrito': carrito})
