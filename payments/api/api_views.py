from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.contenttypes.models import ContentType

from payments.models import Cart, CartItem, Order, OrderItem
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def remove_from_cart_api(request):
    try:
        item_id = request.data.get('item_id')
        quantity = request.data.get('quantity')
        cart_item = CartItem.objects.get(id=item_id, cart__user=request.user)
        
        if cart_item.quantity > int(quantity):
            cart_item.quantity -= int(quantity)
            cart_item.save()
        else:
            cart_item.delete()
        
        cart = Cart.objects.get(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout_api(request):
    try:
        cart = Cart.objects.get(user=request.user)
        # Logic to create an Order from the Cart
        # Over simplified, need to add extra logic to handle payments, etc.
        order = Order.objects.create(user=request.user)
        
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                content_type=item.content_type,
                object_id=item.object_id,
                quantity=item.quantity,
                price=item.content_object.price,
            )
            item.delete()
            
        cart.delete()
        
        return Response({'status': 'success', 'order_id': order.id}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)