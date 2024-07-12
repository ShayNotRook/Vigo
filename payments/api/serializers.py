from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from payments.models import Cart, CartItem, Order, OrderItem


class CartItemSerializer(serializers.ModelSerializer):
    content_object = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'content_object', 'quantity', 'price']
        
    
    def get_content_object(self, obj):
        return obj.content_object.name
    
    def get_price(self, obj):
        return obj.content_object.price
    
    

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'get_total_price']
        
        
    
class OrderItemSerializer(serializers.ModelSerializer):
    content_object = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'content_object', 'quantity', 'price', 'total_price']
        
    def get_content_object(self, obj):
        return obj.content_object.name
    
    def get_total_price(self, obj):
        return obj.total_price
    
    

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id', 'items', 'total_price', 'created_at']
        
    def get_total_price(self, obj):
        return obj.total_price