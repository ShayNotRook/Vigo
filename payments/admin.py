from django.contrib import admin
from .models import Cart, CartItem, Order
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


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    actions = ['mark_as_paid', 'mark_as_completed']
    
    def mark_as_paid(self, request, queryset):
        queryset.update(status='paid')
    mark_as_paid.short_description = 'Mark selected orders as paid'

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = 'Mark selected orders as completed'
    



# Registerars
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)