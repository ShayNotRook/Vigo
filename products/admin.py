from django.contrib import admin

from .forms import GameForm
from .models import (Category, Game, GiftCard, GiftcardKey,
                     Account, SystemRequirement, ProductKey,
                     GameItem)

# Utility Functions

    

# Register your models here.

class SystemRequiredInline(admin.StackedInline):
    model = SystemRequirement
    can_delete = False
    verbose_name_plural = 'System Requirements'

# Game Model Settings
class GameAdmin(admin.ModelAdmin):
    form = GameForm
    inlines = [SystemRequiredInline]
    list_display = ('name', 'category', 'Price')
    
    def Price(self, obj):
        return str(obj.price) + '$'
    
    
    
# Category Model Settings
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('parent', 'slug')
    
    
    
# Gift Card Model Settings
class GiftCardAdmin(admin.ModelAdmin):
    list_display = ('platform', 'value', 'region', 'quantity')
    list_filter = ('platform', 'value', 'region')


class GiftCardKeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'Key', 'giftcard')
    
    def Key(self, obj):
        return obj.key[:9] + "..."


# ProductKey Model Settings
class ProductKeyAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'short_key', 'game', 'redeemed', 'platform')

    def short_key(self, obj):
        return obj.key[:10] + '...'
    
    
    
class GameItemAdmin(admin.ModelAdmin):
    list_display = ('game', 'name', 'quantity', 'Price')
    
    def Price(self, obj):
        return str(obj.price) + '$'
    
    
    
    

# Registerars
admin.site.register(Category, CategoryAdmin)
admin.site.register(GiftCard, GiftCardAdmin)
admin.site.register(GiftcardKey, GiftCardKeyAdmin)
admin.site.register(Account)
admin.site.register(Game, GameAdmin)
admin.site.register(SystemRequirement)
admin.site.register(ProductKey, ProductKeyAdmin)
admin.site.register(GameItem, GameItemAdmin)