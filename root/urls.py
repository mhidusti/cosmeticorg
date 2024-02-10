from django.urls import path,include
from .views import *



app_name = 'root'

urlpatterns = [
    path("",home,name="home"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("product",product,name="product"),
    # path("trainer",trainer,name="trainer"),
    # path('api/V1/', include('restaurant.api.V1.urls')),
]