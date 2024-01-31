from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('api/V1/', include('restaurant.api.V1.urls')),
]