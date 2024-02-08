from django.urls import path,include
from .views import *



app_name = 'root'

urlpatterns = [
    path("",home,name="home"),
    # path('api/V1/', include('restaurant.api.V1.urls')),
]