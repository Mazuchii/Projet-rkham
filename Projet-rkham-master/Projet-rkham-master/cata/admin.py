from django.contrib import admin
from .models import Article, ImageModel, Rating



class ImageModelInline(admin.StackedInline):  
    model = ImageModel
    extra = 0  

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('heading', 'average_rating', 'total_ratings')
    list_filter = ('created_at',)
    search_fields = ('heading',)
    inlines = [ImageModelInline]

@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('img_alt', 'category', 'image', 'created_at')