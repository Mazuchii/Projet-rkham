from django.shortcuts import render
from django.db.models import Avg
from .models import *

# Create your views here.
def index(response):
    return render(response, "cata/index.html", {})
def index1(response):
    return render(response, "cata/index1.html", {})
def top_rated_articles(request):
    articles = Article.objects.annotate(average_rating=Avg('ratings__rating'))
    
    top_articles = articles.filter(average_rating__isnull=False).order_by('-average_rating')[:5] 
    
    context = {
        'catalogue': top_articles,
    }
    return render(request, 'cata/index.html', context)