from django.contrib import admin
from .models import Category,Post
# Register your models here.

#for configuration of Category admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','description','url','add_date','image_tag']
    search_fields=['title']
    icon_name='category'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title']
    search_fields=['title']
    list_filter=['cat']
    list_per_page=50
    icon_name='pages'

    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/script.js',)
