from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, TelegramUser

admin.site.unregister(Group)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'telegram_username', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'telegram_username')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'telegram_username')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    ordering = ('username',)

@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'chat_id', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('username', 'chat_id')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {'fields': ('chat_id', 'username')}),
        ('Metadata', {'fields': ('created_at',)}),
    )

admin.site.site_header = "Task Manager Administration"
admin.site.site_title = "Task Manager Admin Portal"
admin.site.index_title = "Welcome to Task Manager Admin"