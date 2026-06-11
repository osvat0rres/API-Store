from django.urls import path
from . import views

urlpatterns = [
    path('categories/<int:pk>/', views.CategoryView.as_view()),
]
