"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models.autor import Autor
from core.models.categoria import Categoria
from core.models.editora import Editora
from core.models.livro import Livro
from core.models.user import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name", "passage_id", "foto")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
        (_("Groups"), {"fields": ("groups",)}),
        (_("User Permissions"), {"fields": ("user_permissions",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "passage_id"
                ),
            },
        ),
    )


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')
    list_per_page = 10


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)
    list_per_page = 10


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site')
    search_fields = ('nome', 'site')
    list_filter = ('nome', 'site')
    ordering = ('nome', 'site')
    list_per_page = 10


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editora', 'categoria')
    search_fields = ('titulo', 'editora__nome', 'categoria__descricao')
    list_filter = ('editora', 'categoria')
    ordering = ('titulo', 'editora', 'categoria')
    list_per_page = 25
