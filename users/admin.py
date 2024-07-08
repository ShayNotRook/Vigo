from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
User = get_user_model()
from .models import Profile

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'last_login', 'is_superuser', 'is_active')
    
    
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'short_bio')
    
    def short_bio(self, obj):
        return obj.bio[:12] + '...'


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)