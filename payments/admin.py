from typing import Any
from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem
from .forms import CartItemForm
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    
    
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'get_content_object_name', 'quantity', 'get_total_price')
    readonly_fields = ('get_total_price',)
    form = CartItemForm
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        content_type = form.cleaned_data.get('content_type')
        object_id = form.cleaned_data.get('object_id')
        
        if content_type and object_id:
            obj.content_type = content_type.get_object_for_this_type(id=object_id)
        
        super().save_model(request, obj, form, change)
    
    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = 'Total Price'
    
    def get_content_object_name(self, obj):
        return obj.content_object.name
    get_content_object_name.short_description = 'Product'
    
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0 # Remove the extra blank line
    fields = ('content_object', 'quantity', 'price', 'total_price')
    readonly_fields = ('content_object', 'price', 'total_price')
    
    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price'
    


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'updated_at')
    inlines = [OrderItemInline]
    list_filter = ('status',)
    actions = ['mark_as_paid', 'mark_as_completed']
    fieldsets = (
        ('Order Info',
            {'fields': ('user', 'status', 'updated_at', 'created_at')}),
    )
    readonly_fields = ('user', 'created_at', 'updated_at', 'total_price')
    
    def mark_as_paid(self, request, queryset):
        queryset.update(status='paid')
    mark_as_paid.short_description = 'Mark selected orders as paid'

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
    mark_as_completed.short_description = 'Mark selected orders as completed'
    
    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price'
    



# Registerars
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)