from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem, Category, Cart, Order, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'tittle', 'slug']

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    
    class Meta:
        model = MenuItem
        fields = ['id', 'tittle', 'featured', 'price', 'category']

class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset= User.objects.all(),
        default = serializers.CurrentUserDefault()
    )
    
    def validate(self,atts):
        atts['price'] = atts['quantiry'] * atts['unit_pice']
        
        
    class Meta:
        model = Cart
        fields = ['user', "menuitem", "quantity", "price",'unit_price']
        #This means that the client cannot provide there own value fro price
        extra_kwargs = {'price' : {'read_only' : True}}
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [ 'order',  'menuItem', 'quantity', 'price']
        
        
        
class OrderSerializers(serializers.ModelSerializer):
    OrderItems = OrderItemSerializer(many=True, read_only = True, source='order')
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status','date','total', 'orderitem']
        
        
class UserSericalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
