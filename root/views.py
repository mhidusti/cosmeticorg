from typing import Any
from django.shortcuts import render , redirect, get_object_or_404, redirect
from django.views import View
from .models import *
from django.contrib import messages
from django.views.generic import ListView,TemplateView,DetailView
from .forms import ContactUsForm,CommentForm





# def home(request):
#     # if request.method == 'GET':
#     #     category = Category.objects.all()
#     #     productFeature = Product_Feature.objects.filter(status = True)
#     #     bestproducts = Best_Products.objects.filter(status = True)
#     #     products = Products.objects.filter(status = True)
#     #     special = Special_Products.objects.filter(status = True)
#     #     pack = Pack_Products.objects.filter(status = True)
#     #     gallery = Gallery.objects.all()
#     #     social= Social.objects.filter(status = True)
#     #     context = {
#     #          'category': category,
#     #          'pf': productFeature,
#     #          'bp': bestproducts,
#     #          'products': products,
#     #          'special': special,
#     #          'pack': pack,
#     #          'gallery': gallery,
#     #          'social': social,
            
#     #         }
#     return render(request,"root/index.html")

# def about (request):
#     return render(request,"root/about.html")


class HomeListView(ListView):
    template_name = "root/index.html"
    context_object_name = 'product_feature'
    queryset = Product_Feature.objects.filter(status = True)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['best_product'] = Best_Products.objects.filter(status = True)
        context['gallery'] = Gallery.objects.filter(status = True)
        context['social'] = Social.objects.filter(status = True)
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your comment')
            return redirect('root:home')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid data please try again')
            return redirect('root:home')

    # def get_context_data(self, **kwargs: Any): 
    #     context = super().get_context_data(**kwargs)
    #     context['gallery'] = Gallery.objects.filter(status = True)
    #     return context
    
    # def get_context_data(self, **kwargs: Any): 
    #     context = super().get_context_data(**kwargs)
    #     context['social'] = Social.objects.filter(status = True)
    #     return context





class AboutListView(ListView):
    template_name = "root/about.html"
    context_object_name = 'productt'
    queryset = Product_Feature.objects.filter(status = True)




class ContactListView(ListView):
    model = ContactUs
    template_name = 'root/contact.html'
    
    def post(self, request, *args, **kwargs):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you as soon')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')
        




# def contact(request):
#     if request.method == 'POST':
#         form = ContactUsForm(request.POST)
#         if form.is_valid():
#             form.save()  
#             messages.add_message(request,messages.SUCCESS,'we received your message and call with you as soon')
#             return redirect('root:contact')   
#         else :
#             messages.add_message(request,messages.ERROR,'Invalid data')
#             return redirect('root:contact')

#     return render(request,"root/contact.html")













