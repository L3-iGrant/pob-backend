from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from igrant_user.models import IGrantUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = IGrantUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = IGrantUser
        fields = ("email",)


class IGrantUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = IGrantUser
    list_display = (
        "email",
        "is_staff",
        "is_active",
        "user_type",
        "org",
        "org_verification_status",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
        "user_type",
        "org",
        "org_verification_status",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "user_type",
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
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "user_type",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(IGrantUser, IGrantUserAdmin)
