from django.db import models

from django.utils.translation import gettext as _
from django.contrib import admin



from sevo_core import models as core_models

class Category(core_models.TimeStampMixin):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = [
            "name",
        ]


class Tag(core_models.TimeStampMixin):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = [
            "name",
        ]
    
class Post(core_models.TimeStampMixin, core_models.BaseUserMixin):
    title = models.CharField(max_length=255, verbose_name=_("Title"))

    keywords = models.CharField(max_length=255, verbose_name=_("Keywords"))
    description = models.CharField(max_length=255, verbose_name=_("Description"))   



    content = models.TextField(verbose_name=_("Content"))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Category"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Tags"))      
    is_featured = models.BooleanField(default=False, verbose_name=_("Is Featured")) 
    alow_comments = models.BooleanField(default=True, verbose_name=_("Allow Comments")) 
    show_coments = models.BooleanField(default=True, verbose_name=_("Show Comments"))   
    is_published = models.BooleanField(default=False, verbose_name=_("Is Published"))   
    

    @admin.display(description=_("Tags"))
    def get_tags_as_string(self):
        return ", ".join([tag.name for tag in self.tags.all()]) 
    

    def __str__(self):
        return self.title   
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = [
            "-created_at",
        ]
