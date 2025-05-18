from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "name",
        "last_name",
        "phone_number",
        "email",
        "is_verified",
        "access_level",
        "balance",
    )
    fieldsets = (
        (None, {"fields": ("username", "email", "password", 'balance')}),
        ("Персональная информация", {"fields": ("name", "last_name", "phone_number")}),
        (
            "Разрешения",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        (
            "Additional info",
            {
                "fields": (
                    "is_verified",
                    "access_level",
                    "date_of_birth",
                    "gender",
                    "address",
                    "visits_count",
                    "activity_history",
                    "is_subscribed",
                    "preferred_contact_method",
                    "transaction_history",
                    "loyalty_discount",
                    "allergies",
                    "special_notes",
                    "social_media_links",
                    "referral_code",
                    "source_of_signup",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "name",
                    "last_name",
                    "phone_number",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    ordering = ("email",)
