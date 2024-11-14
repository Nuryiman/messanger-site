from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser, Chat, UserMessage


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['phone_number', 'first_name']
    ordering = ['phone_number',]

    search_fields = ("first_name", "last_name", "phone_number")
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "birth_day",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "password1", "password2"),
            },
        ),
    )


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'user1', 'user2']


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'text']

