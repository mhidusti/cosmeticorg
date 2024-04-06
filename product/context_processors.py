from .cart import Cart
from .wish import Wish

def cart(request):
    cart = Cart(request)
    return {'cart':cart}



def wish(request):
    wish = Wish(request)
    return {'wish':wish}