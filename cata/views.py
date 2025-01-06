from django.db.models import Avg
from .models import *
from django.shortcuts import render , redirect
from django.core.paginator import Paginator
from .models import Article
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .models import Comment

@login_required
def add_comment(request):
    if request.method == "POST":
        message = request.POST.get("message")
        if message:
            Comment.objects.create(user=request.user, message=message)
        return redirect("index")  # Replace with the name of your home page
    return redirect("index")

def catalog(request):
    articles = Article.objects.prefetch_related('image').all()  
    return render(request, 'catalog.html', {'articles': articles})


def about(request):
    videos = Videomodel.objects.select_related('category').all()  # Fetch all videos with their categories
    return render(request, "about.html", {'videos': videos})
def index(response):
    return render(response, "index.html", {})

def index1(response):
    return render(response, "index1.html", {})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def catalog(request):
    articles_list = Article.objects.prefetch_related('image').all()
    paginator = Paginator(articles_list, 2)

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

    return render(request, 'catalog.html', {'articles': articles})





def logout(request):
    auth_logout(request)
    return redirect('index')