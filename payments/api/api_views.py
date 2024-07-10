from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.contenttypes.models import ContentType

from payments.models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart_api(request):
    content_type_id = request.data.get('content_type_id')
    object_id = request.data.get('object_id')
    content_type = ContentType.objects.get(id=content_type_id)
    product = content_type.get_object_for_this_type(id=object_id)
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        content_type=content_type,
        object_id=object_id,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_details_api(request):
    cart = Cart.objects.get(user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data)