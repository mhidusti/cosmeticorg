from django.urls import path,include
from .views  import *

app_name = 'product'

urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('cart',CartView.as_view(), name='cart'),
    path("search/",ProductView.as_view(),name="product_search"),
    path("category/<str:cat>",ProductView.as_view(),name="product_cat"),
    path("wish/",wishView.as_view(),name="wish"),
    
]