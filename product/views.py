from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView,TemplateView
from .cart import Cart
from .models import Products,Category





class ProductView(ListView):
    
    template_name = 'product/product.html'
    context_object_name = 'product'
    paginate_by = 6

    def get_queryset(self):
        if self.kwargs.get('cat'):
            return Products.objects.filter(category__name=self.kwargs.get('cat'))
        
        elif self.request.GET.get('search'):
            return Products.objects.filter(content__contains = self.request.GET.get('search'))
        else:
            return Products.objects.filter(status=True) 
    def post(self, request, *args, **kwargs):
        post_detail = ProductDetailView()
        return post_detail.post(request,*args,**kwargs)




class ProductDetailView(DetailView):
    model = Products
    template_name = 'product/detail.html'
    context_object_name = 'product'

    
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        
        if 'id' in request.POST :
            product = get_object_or_404(Products, id=request.POST['id'])    
            cart.delete_from_cart(product)
            
        else:
            product = get_object_or_404(Products, id=request.POST['pk'])
            cart.add_to_cart_one_quantity(product)

        return redirect(request.path_info)
       
class CartView(TemplateView):
    template_name = 'product/cart.html'

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return redirect(request.path_info)