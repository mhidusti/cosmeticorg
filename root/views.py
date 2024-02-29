from typing import Any
from django.shortcuts import render , redirect, get_object_or_404, redirect
from django.views import View
from .models import *
from django.contrib import messages
from django.views.generic import ListView,TemplateView,DetailView
from .forms import ContactUsForm,CommentForm





class HomeListView(ListView):
    template_name = "root/index.html"
    context_object_name = 'product_feature'
    queryset = Product_Feature.objects.filter(status = True)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['special_products'] = Special_Products.objects.filter(status = True)
        context['pack_products'] = Pack_Products.objects.filter(status = True)
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
        















