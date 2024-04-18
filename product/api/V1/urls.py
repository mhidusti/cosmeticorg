from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('courses', ProductView, basename='product')
router.register('category', CategoryView, basename='category')
urlpatterns = router.urls





# urlpatterns = [
#     path("courses/",CourseView.as_view({'get': 'list', 'post':'create'}),name='courses'),
#     path("courses/<int:pk>/",CourseView.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}),name='course-detail'),

# ]