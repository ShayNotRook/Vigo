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

admin.site.register(Category)
admin.site.register(GiftCard)
admin.site.register(Account)
admin.site.register(Game, GameAdmin)
admin.site.register(SystemRequirement)