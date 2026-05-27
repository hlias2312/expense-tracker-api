from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'expenses', views.ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', obtain_auth_token, name='api_token_auth'),
]