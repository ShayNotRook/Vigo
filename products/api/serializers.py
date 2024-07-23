from rest_framework import serializers

from products.models import Game, GiftCard, Category, Product, GameItem


class CategorySerialzer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail', lookup_field='slug')
    subcategories = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'title', 'url', 'slug', 'subcategories', 'products']
        
    def get_subcategories(self, obj):
        subcategories = obj.get_subcategories()
        if subcategories.exists():
            return CategorySerialzer(subcategories, many=True, context=self.context).data
        return []
    
    def get_products(self, obj):
        products = obj.get_all_products()
        if products:
            return ProductSerializer(products, many=True, context=self.context).data
        return []
        
class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Game
        fields = ['id', 'name', 'price', 'description', 'category', 'image_url']
    
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None    
        

class GameSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = Game
        

class GiftCardSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = GiftCard
        
        
class GameItemSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = GameItem
        
        
class ItemSerializer(serializers.Serializer):
    def to_representation(self, instance):
        if isinstance(instance, Game):
            serializer = GameSerializer(instance, context=self.context)
        elif isinstance(instance, GiftCard):
            serializer = GiftCardSerializer(instance, context=self.context)
        elif isinstance(instance, GameItem):
            serializer = GameItemSerializer(instance, context=self.context)