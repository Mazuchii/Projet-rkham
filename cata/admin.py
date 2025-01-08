from django.contrib import admin
from .models import Article, ImageModel, Category, Videomodel, Comment
from django.shortcuts import render, redirect
from django.contrib import messages

# Define the custom action to assign a category to selected articles
def assign_category_to_articles(modeladmin, request, queryset):
    if 'apply' in request.POST:
        # Get the category selected in the form
        category_name = request.POST.get('category')
        if not category_name:
            modeladmin.message_user(request, "No category selected.", level=messages.ERROR)
            return

        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            modeladmin.message_user(request, f"Category '{category_name}' does not exist.", level=messages.ERROR)
            return

        # Assign the category to selected articles
        queryset.update(category=category)
        modeladmin.message_user(request, f"Category '{category_name}' has been assigned to selected articles.", level=messages.SUCCESS)
        return redirect(request.get_full_path())

    # If no category is selected, show the form to select one
    categories = Category.objects.all()
    
    return render(request, 'admin/select_category_form.html', {
        'categories': categories,
        'action': 'assign_category_to_articles',
        'selected': queryset.values_list('uid', flat=True),
        'opts': modeladmin.model._meta,
    })

assign_category_to_articles.short_description = "Assign category to selected articles"

class ImageModelInline(admin.StackedInline):
    model = ImageModel
    extra = 0

@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('img_alt', 'image_preview', 'created_at', 'updated_at')  
    readonly_fields = ('image_preview',)  
    search_fields = ('img_alt',)

    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')
    search_fields = ('user__username', 'message')

@admin.register(Videomodel)
class VideomodelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'category_display')
    search_fields = ('name', 'category__name')
    inlines = [ImageModelInline]
    actions = [assign_category_to_articles]

    def category_display(self, obj):
        return obj.category.name if obj.category else "No Category"
    category_display.short_description = 'Category'
