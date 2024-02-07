from django.shortcuts import render , redirect, get_object_or_404, redirect
from django.views import View
from .models import *
# from django.contrib import messages
from django.views.generic import ListView
from .cart import Cart

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'root/index.html')
        



# class HomeListView(ListView):
    
#     template_name = 'root/index.html'
#     context_object_name = 'root'
    

#     def get_queryset(self):
#         if self.kwargs.get('cat'):
#             return Products.objects.filter(category__name=self.kwargs.get('cat'))
        
#         else:
#             return Products.objects.filter(status=True) 
        
#     def post(self, request, *args, **kwargs):
#         cart = Cart(request)
        
#         if 'id' in request.POST :
#             product = get_object_or_404(Products, id=int(request.POST['id']))    
#             cart.delete_from_cart(product)
            
#         else:
#             product = get_object_or_404(Products, id=int(request.POST['pk']))
#             quantity = int(request.POST['quantity'])
#             cart.add_to_cart_some_quantity(product, quantity)
            
#         return redirect(request.path_info)






# def home(request):
#     if request.method == 'GET':
#         category = Category.objects.all()
#         Productfeature = Product_Feature.objects.filter(status = True)
#         Bestproducts = Best_Products.objects.filter(status = True)
#         Products = Products.objects.filter(status = True)
#         Special = Special_Products.objects.filter(status = True)
#         Pack = Pack_Products.objects.filter(status = True)
#         Gallery = Gallery.objects.all()
#         Social= Social.objects.filter(status = True)
#         context = {
#              'category': Category,
#              'pf': Product_Feature,
#              'bp': Best_Products,
#              'Products': Products,
#              'Special': Special_Products,
#              'Pack': Pack_Products,
#              'Gallery': Gallery,
#              'Social': Social,
            
#             }
#         return render(request,"root/index.html",context=context)

#     elif request.method == 'POST':
#         form = ContactUsForm(request.POST)
#         if form.is_valid():

#             form.save()  
#             messages.add_message(request,messages.SUCCESS,'we received your message and call with you you as soon MYDAER')
#             return redirect('root:home')
#     else:
#             messages.add_message(request,messages.ERROR,'ur data is invalid plz check them and try again')
#             return redirect('root:home')


