from django.contrib import admin

from sevo_blog import models
from sevo_core.admin import BaseUserAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]

    list_display_links = [
        "id",
        "name",
    ]



class TagAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]

    list_display_links = [
        "id",
        "name",
    ]


class PostAdmin(BaseUserAdmin):
    list_display = [
        "id",
        "user",
        "title",
        "category",
        "get_tags_as_string",
        "is_featured",
        "is_published",
        "created_at",
        "updated_at",
    ]

    list_display_links = [
        "id",
        "user",
        "title",
    ]

    search_fields = [
        "title",
        "content",
    ]

    list_filter = [
        "is_published", 
        "created_at",
        "updated_at",
        "category",
        "tags",
        "user",
        "is_featured",
        "alow_comments",
        "show_coments",
    ]

    list_editable = [
        "is_published",
        "is_featured",
    ]





admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag)
