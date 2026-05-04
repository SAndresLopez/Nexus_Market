from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='add_cart'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('restar/<int:producto_id>/', views.restar_del_carrito, name='sub_cart'),
]