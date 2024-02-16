from django.urls import path,include
from .views  import *

app_name = 'product'

urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('product-detail/', ProductDetailView.as_view(), name='product_detail'),
    path('cart',CartView.as_view(), name='cart'),
    
]