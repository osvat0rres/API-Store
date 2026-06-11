from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreateAPIView.as_view()),
    path('products/', views.ProductsListCreateAPIView.as_view())
]