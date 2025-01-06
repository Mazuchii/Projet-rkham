from django.contrib import admin
from .models import Article, ImageModel, Category, Videomodel
from .models import Comment


class ImageModelInline(admin.StackedInline):
    model = ImageModel
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')
    search_fields = ('user__username', 'message')

@admin.register(Videomodel)
class VideomodelAdmin(admin.ModelAdmin):
    list_display = ('name' , 'created_at', 'updated_at')
    search_fields = ('name',)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    inlines = [ImageModelInline]


