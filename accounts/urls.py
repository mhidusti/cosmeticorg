from django.urls import path,include
from .views import *


app_name = 'accounts'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]