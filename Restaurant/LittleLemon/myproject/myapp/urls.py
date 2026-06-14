from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesView.as_view()),
    path('cart/menu-items/', views.CartView.as_view()),
    path('menuitems/', views.MenuItemsView.as_view()),
    path('menuitems/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('orders/', views.OrderView.as_view()),

]

#CartegoryView
#CartView
#MenuItemsView
#SingleMenuItemView
#OrderView
