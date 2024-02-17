from django.urls import path,include
from .views import *


app_name = 'root'

urlpatterns = [
    path("",home,name="home"),
    path("about",AboutListView.as_view(),name="about"),
    path("contact",ContactListView.as_view(),name="contact"),
    # path("trainer",trainer,name="trainer"),

]






