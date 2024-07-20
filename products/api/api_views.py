from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from products.models import Category, Game, GiftCard

from .serializers import GameSerializer, GiftCardSerializer, CategorySerialzer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzer
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'games':
            return GameSerializer
        elif self.action == 'giftcards':
            return GiftCardSerializer
        return super().get_serializer_class()
    
    
    @action(detail=True, methods=['get'])
    def products(self, request, slug=None):
        category = self.get_object()
        response_data = {}
        
        products = category.get_all_products()
        if products:
            response_data['products'] = ProductSerializer(products, many=True, context=self.get_serializer_context()).data
        
        subcategories = category.get_subcategories()
        if subcategories.exists():
            response_data['subcategories'] = CategorySerialzer(subcategories, many=True, context=self.get_serializer_context()).data
        
        return Response(response_data)
    
    # @action(detail=True, methods=['get'])
    # def games(self, request, slug=None):
    #     category = self.get_object()
    #     games = Game.objects.filter(category=category)
    #     serializer = GameSerializer(games, many=True)
    #     return Response(serializer.data)
    
    
    # @action(detail=True, methods=['get'])
    # def giftcards(self, request, slug=None):
    #     category = self.get_object()
    #     giftcards = GiftCard.objects.filter(category=category)
    #     serializer = GiftCardSerializer(giftcards, many=True)
    #     return Response(serializer.data)
        
        # games = Game.objects.filter(category=category)
        # if games.exists():
        #     products['games'] = GameSerializer(games, many=True).data
            
        # giftcards = GiftCard.objects.filter(category=category)
        # if giftcards.exists():
        #     products['giftcards'] = GiftCardSerializer(giftcards, many=True).data
        
        # return Response(products)
    