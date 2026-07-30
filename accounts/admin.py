
from django.contrib import admin
from django.contrib.auth.models import UserAdmin
from .models import User

@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_active')
    lisyt_filter = ('role', 'is_active')
    
    
    fieldsets = UserAdmin.fieldsets + (
        ('Profie', {'fields': ('role', 'bio', 'avatar')})
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Profile', {'fields': ('role', 'bio', 'avatar')})
    )