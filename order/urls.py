from django.urls import path
from .views import *


app_name = 'order'

urlpatterns = [
    path('', CreateOrderByView.as_view(), name='order')
    
]