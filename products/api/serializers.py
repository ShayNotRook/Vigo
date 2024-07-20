from rest_framework import serializers

from products.models import Game, GiftCard, Category, Product


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
    class Meta:
        model = Game
        fields = '__all__'

class GameSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = Game
        

class GiftCardSerializer(serializers.ModelSerializer):
    class Meta(ProductSerializer.Meta):
        model = GiftCard