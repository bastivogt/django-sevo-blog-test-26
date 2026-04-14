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


class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "get_image_tag",
        "title",
        "created_at",
        "updated_at",
    ]

    list_display_links = [
        "id",
        "get_image_tag",
        "title",
    ]

    fields = [
        "title",
        "image",
        "get_image_tag_link",
    ]

    readonly_fields = [
        "get_image_tag_link",
    ]


class PostAdmin(BaseUserAdmin):
    fields = [
        "user",
        "title",
        "content",
        "category",
        "tags",
        "image",
        "get_image_tag",
        "keywords",
        "description",
        "is_featured",
        "alow_comments",
        "show_coments",
        "is_published",
    ]   
    list_display = [
        "id",
        "title",
        "get_image_tag",
        "category",
        "get_tags_as_string",
        "is_featured",
        "is_published",
        "created_at",
        "updated_at",
        "user",
    ]

    list_display_links = [
        "id",
        "user",
        "title",
        "get_image_tag",
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

    readonly_fields = [
        "get_image_tag",
    ]

    raw_id_fields = [
        "image",
    ]

    def get_list_filter(self, request):
        filters = list(self.list_filter)
        print("user_field_name: ", self.user_field_name)
        if request.user.is_superuser:
            if self.user_field_name not in filters:
                filters.append(self.user_field_name)
        else:
            filters = [f for f in filters if f != self.user_field_name]
        return filters






admin.site.register(models.Post, PostAdmin)
admin.site.register(models.PostImage, PostImageAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
