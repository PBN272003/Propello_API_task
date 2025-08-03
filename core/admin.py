from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Firm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Firm)
