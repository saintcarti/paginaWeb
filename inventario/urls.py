from django.urls import path
from .views import *

urlpatterns = [
    path('mercado/', inventario_view, name='inventario'),
    path('API/', API, name='API'),
    path('inventario_stock/',listado_camaras, name='listado_camaras'),
    path('inventario_stock/detalle_camara/<int:id>/',detalle_camara, name= 'detalle_camara'),
    path('inventario_stock/crear_camara/',crear_camara, name= 'crear_camara'),
    path('inventario_stock/editar_camara/<int:id>/',editar_camara, name= 'editar_camara'),
    path('inventario_stock/eliminar_camara/<int:id>/',eliminar_camara, name= 'eliminar_camara'),
    path('mercado/agregar/<id>/',agregar_producto, name='agregar'),
    path('mercado/eliminar/<id>/',eliminar_producto, name='eliminar'),
    path('mercado/restar/<id>/',restar_producto, name='restar'),
    path('mercado/limpiar/',limpiar_carrito, name='limpiar'),
    path('mercado/generarBoleta/',generarBoleta, name='generarBoleta'),


]
