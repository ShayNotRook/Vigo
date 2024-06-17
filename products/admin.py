from django.contrib import admin

from .forms import GameForm
from .models import (Category, Game, GiftCard, Account, SystemRequirement, ProductKey)
# Register your models here.

class SystemRequiredInline(admin.StackedInline):
    model = SystemRequirement
    can_delete = False
    verbose_name_plural = 'System Requirements'

# Game Model Settings
class GameAdmin(admin.ModelAdmin):
    form = GameForm
    inlines = [SystemRequiredInline]
    list_display = ('name', 'category', 'price')
    
    
    
# Category Model Settings
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('parent', 'slug')
    
    
    
# Gift Card Model Settings
class GiftCardAdmin(admin.ModelAdmin):
    list_display = ('platform', 'value', 'region', 'quantity')
    list_filter = ('platform', 'value', 'region')



# ProductKey Model Settings
class ProductKeyAdmin(admin.ModelAdmin):
    list_display = ('short_key', 'game', 'redeemed', 'platform')

    def short_key(self, obj):
        return obj.key[:10] + '...'
    
    

# Registerars
admin.site.register(Category, CategoryAdmin)
admin.site.register(GiftCard, GiftCardAdmin)
admin.site.register(Account)
admin.site.register(Game, GameAdmin)
admin.site.register(SystemRequirement)
admin.site.register(ProductKey, ProductKeyAdmin)