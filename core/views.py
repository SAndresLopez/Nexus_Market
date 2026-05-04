from django.shortcuts import render, get_object_or_404,redirect
from .models import Producto
from .cart import Cart

def home(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()

    return render(request, 'core/home.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'core/detalle.html', {'producto': producto})

def agregar_al_carrito(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.add(producto=producto)
    return redirect('ver_carrito')

def ver_carrito(request):
    return render(request, 'core/carrito.html')

def restar_del_carrito(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id=producto_id)
    cart.decrement(producto=producto)
    return redirect('ver_carrito')