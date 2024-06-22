from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
User = get_user_model()

# Register your models here.

# class UserAdmin(BaseUserAdmin):
#     pass


admin.site.register(User, UserAdmin)
