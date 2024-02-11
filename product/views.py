from django.shortcuts import render
from django.views import View

class ProductView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'product/product.html')
        

class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'product/detail.html')
        
