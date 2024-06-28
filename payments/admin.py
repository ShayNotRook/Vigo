from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    
    
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'get_content_object_name', 'quantity', 'get_total_price')
    readonly_fields = ('get_total_price',)
    
    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = 'Total Price'
    
    def get_content_object_name(self, obj):
        return obj.content_object.name
    get_content_object_name.short_description = 'Product'


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)