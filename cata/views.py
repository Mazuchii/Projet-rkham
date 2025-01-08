
from .models import *
from django.shortcuts import render , redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

@login_required
def add_comment(request):
    if request.method == "POST":
        message = request.POST.get("message")
        if message:
            Comment.objects.create(user=request.user, message=message)
        return redirect("index1")  # Replace with the name of your home page
    return redirect("index1")




def about(request):
    videos = Videomodel.objects.select_related('category').all()  
    return render(request, "about.html", {'videos': videos})

def index1(response):
    return render(response, "index1.html", {})

from django.core.paginator import Paginator, EmptyPage

def catalog(request):
    articles_list = Article.objects.prefetch_related('image').all()
    categories = Category.objects.all() 

    category_name = request.GET.get('category')
    if category_name:
        try:
            selected_category = Category.objects.get(name=category_name)
            articles_list = articles_list.filter(category=selected_category)  
        except Category.DoesNotExist:
            articles_list = Article.objects.none()  

    # Handle pagination
    paginator = Paginator(articles_list, 12)
    page_number = request.GET.get('page')

    try:
        page_number = int(page_number) if page_number else 1
        if page_number < 1:
            raise ValueError("Page number must be >= 1")
    except (ValueError, TypeError):
        page_number = 1

    try:
        articles = paginator.page(page_number)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'catalog.html', {'articles': articles, 'categories': categories})






def logout(request):
    auth_logout(request)
    return redirect('index1')