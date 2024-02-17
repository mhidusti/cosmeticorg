from django.shortcuts import render , redirect, get_object_or_404, redirect
from django.views import View
from .models import *
from django.contrib import messages
from django.views.generic import ListView,TemplateView,DetailView
from .forms import ContactUsForm





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

# def about (request):
#     return render(request,"root/about.html")


class AboutListView(ListView):

    template_name = 'root/about.html'
    context_object_name = 'product'
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













