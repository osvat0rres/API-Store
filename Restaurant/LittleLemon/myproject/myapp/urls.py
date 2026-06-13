from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('cart/', views.CartView.as_view()),
    path('menuitems/', views.MenuItemsView.as_view()),
    path('menuitems/<int:pk>/', views.SingleMenuItemView.as_view()),

]
