from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, CartSerializer, MenuItemSerializer, OrderSerializers
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.shortcuts import  get_object_or_404
from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from rest_framework import status
# Create your views here.

    
#This will create a category input
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'POST':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


#This allows authenticated users to see the items in their cart and add new ones
class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Cart.objects.all().filter(user=self.request.user)
    
    #It allows items to be deleted form the cart
    def delete(self, request, *args, **kwargs):
        Cart.objects.all().filter(user=self.request.user).delete()
        return Response("All items were deleted")
    

#This will create a new item        
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields = ['category_tittle']
    ordering_fields = ['price']
    
    def get_permissions(self):
        permission_classes = [ ]
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

#This will allow users to rertrieve, update or delete a single item
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_class = [IsAuthenticated]
    
    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_class = [IsAuthenticated]
