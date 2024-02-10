from django.shortcuts import render , redirect, get_object_or_404, redirect
from django.views import View
from .models import *
# from django.contrib import messages
from django.views.generic import ListView,TemplateView,DetailView
from .cart import Cart




def home(request):
    # if request.method == 'GET':
    #     category = Category.objects.all()
    #     productFeature = Product_Feature.objects.filter(status = True)
    #     bestproducts = Best_Products.objects.filter(status = True)
    #     products = Products.objects.filter(status = True)
    #     special = Special_Products.objects.filter(status = True)
    #     pack = Pack_Products.objects.filter(status = True)
    #     gallery = Gallery.objects.all()
    #     social= Social.objects.filter(status = True)
    #     context = {
    #          'category': category,
    #          'pf': productFeature,
    #          'bp': bestproducts,
    #          'products': products,
    #          'special': special,
    #          'pack': pack,
    #          'gallery': gallery,
    #          'social': social,
            
    #         }
    return render(request,"root/index.html")

def about (request):
    return render(request,"root/about.html")

def product(request):
    return render(request, "root/product.html")


def contact(request):
   return render(request,"root/contact.html")



def social(request):
    return redirect('root:social')












