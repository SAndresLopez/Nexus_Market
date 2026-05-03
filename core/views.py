from django.shortcuts import render, get_object_or_404
from .models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, 'core/home.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'core/detalle.html', {'producto': producto})