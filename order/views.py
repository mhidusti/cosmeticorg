
from django.shortcuts import redirect
from .forms import OrderByFrom
from django.views.generic import CreateView
from product.cart import Cart
from .models import OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateOrderByView(LoginRequiredMixin, CreateView):
     template_name = 'order/orderby.html'
     form_class = OrderByFrom

     def form_valid(self, form):
          cart = Cart(self.request)
          order = form.save(commit=False)
          order.user = self.request.user
          order.save()
          for item in cart:
               product = item['product_object']
               OrderItem.objects.create(
                    order = order,
                    product = product,
                    quantity = item['quantity'],
                    price = product.price,
               )
          cart.clear()
          self.request.session['order_id'] = order.id
          return redirect("payment:request")

