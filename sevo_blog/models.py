from django.db import models

from django.utils.translation import gettext as _
from django.contrib import admin
from django.utils import html



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



class PostImage(core_models.TimeStampMixin):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    image = models.ImageField(upload_to="post_images/", verbose_name=_("Image"))

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.image.delete(save=False)  # Delete the image file from storage
        super().delete(*args, **kwargs)  # Call the parent delete method to delete the model instance   

    def get_image_tag(self):
        if self.image:
            return html.format_html('<img src="{}" style="width: 80px; height: 80px; object-fit: cover;" />', self.image.url)
        return ""
    get_image_tag.short_description = _("Image Preview")
    get_image_tag.allow_tags = True  


    def get_image_tag_link(self):
        if self.image:
            return html.format_html('<a href="{}" target="_blank">{}</a>', self.image.url, self.get_image_tag())
        return ""   
    get_image_tag_link.short_description = _("Image Preview")
    get_image_tag_link.allow_tags = True  


    def get_image_url(self):
        if self.image:
            return self.image.url
        return ""
    get_image_url.short_description = _("Image URL")
    get_image_url.allow_tags = True 




    class Meta:
        verbose_name = _("Post Image")
        verbose_name_plural = _("Post Images")
        ordering = [
            "-created_at",
        ]   


    

    
class Post(core_models.TimeStampMixin, core_models.BaseUserMixin):
    title = models.CharField(max_length=255, verbose_name=_("Title"))

    image = models.ForeignKey(PostImage, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Image"))

    keywords = models.CharField(max_length=255, blank=True, null=True,verbose_name=_("Keywords"))
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Description"))   



    content = models.TextField(verbose_name=_("Content"))

    
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Category"))
    categories = models.ManyToManyField(Category, blank=True, verbose_name=_("Categories"))
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=_("Tags"))      
    is_featured = models.BooleanField(default=False, verbose_name=_("Is Featured")) 
    alow_comments = models.BooleanField(default=True, verbose_name=_("Allow Comments")) 
    show_coments = models.BooleanField(default=True, verbose_name=_("Show Comments"))   
    is_published = models.BooleanField(default=False, verbose_name=_("Is Published"))   
    

    def get_categories_as_string(self):
        return ", ".join([category.name for category in self.categories.all()])
    get_categories_as_string.short_description = _("Categories")    
    

    #@admin.display(description=_("Tags"))
    def get_tags_as_string(self):
        return ", ".join([tag.name for tag in self.tags.all()]) 
    get_tags_as_string.short_description = _("Tags")
    

    def get_short_content(self, length=100):
        if len(self.content) > length:
            return self.content[:length] + "..."
        return self.content
    get_short_content.short_description = _("Short Content")    
    

    def get_image_url(self):
        if self.image:
            return self.image.get_image_url()
        return ""
    get_image_url.short_description = _("Image URL")
    get_image_url.allow_tags = True 


    def get_image_tag(self):
        if self.image:
            return self.image.get_image_tag()
        return ""
    get_image_tag.short_description = _("Image Preview")
    get_image_tag.allow_tags = True 

    def get_user_name(self):
        if self.user:
            return self.user.username
        return ""
    get_user_name.short_description = _("Author")   

    def get_test(self):
        return "test"
    get_test.short_description = _("Test")
    get_test.allow_tags = True



    def __str__(self):
        return self.title   
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = [
            "-created_at",
        ]
