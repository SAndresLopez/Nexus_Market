class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.cart:
            self.cart[producto_id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad': 1,
                'imagen': producto.imagen.url if producto.imagen else ""
            }
        else:
            self.cart[producto_id]['cantidad'] += 1
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.save()

    def decrement(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            self.cart[producto_id]['cantidad'] -= 1
            if self.cart[producto_id]['cantidad'] < 1:
                self.remove(producto)
            self.save()

    def get_total_price(self):
        return sum(float(item['precio']) * item['cantidad'] for item in self.cart.values())