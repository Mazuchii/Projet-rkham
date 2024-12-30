from django.contrib import admin
from django.contrib import admin
from .models import Article, ImageModel


class ImageModelInline(admin.TabularInline):
    model = ImageModel
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('heading', 'created_at', 'updated_at')
    inlines = [ImageModelInline]  


@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('img_alt', 'category', 'image', 'created_at')
