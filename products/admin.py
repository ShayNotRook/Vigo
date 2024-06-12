from django.contrib import admin

from .forms import GameForm
from .models import (Category, Game, GiftCard, Account, SystemRequirement)
# Register your models here.

class SystemRequiredInline(admin.StackedInline):
    model = SystemRequirement
    can_delete = False
    verbose_name_plural = 'System Requirements'


class GameAdmin(admin.ModelAdmin):
    form = GameForm
    inlines = [SystemRequiredInline]
    
    
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('parent', 'slug')
    
    

class GiftCardAdmin(admin.ModelAdmin):
    list_display = ('platform', 'value', 'region', 'quantity')
    list_filter = ('platform', 'value', 'region')



# Registerars
admin.site.register(Category, CategoryAdmin)
admin.site.register(GiftCard, GiftCardAdmin)
admin.site.register(Account)
admin.site.register(Game, GameAdmin)
admin.site.register(SystemRequirement)