from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from payments.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    content_object = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'content_object', 'quantity']
        
    
    def get_content_object(self, obj):
        return obj.content_object.name
    
    

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'get_total_price']