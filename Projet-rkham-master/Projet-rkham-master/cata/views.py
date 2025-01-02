from django.db.models import Avg
from .models import *
from django.shortcuts import render , redirect
from django.core.paginator import Paginator
from .models import Article
from django.contrib.auth.decorators import login_required


def catalog(request):
    articles = Article.objects.prefetch_related('image').all()  
    return render(request, 'catalog.html', {'articles': articles})



def index1(response):
    return render(response, "index1.html", {})
def top_rated_articles(request):
    articles = Article.objects.annotate(average_rating=Avg('ratings__rating'))
    
    top_articles = articles.filter(average_rating__isnull=False).order_by('-average_rating')[:5] 
    
    context = {
        'catalogue': top_articles,
    }
    return render(request, 'index1.html', context)

from django.contrib import messages

@login_required
def rate_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        rating_value = request.POST.get('rating')

        existing_rating = Rating.objects.filter(user=request.user, article=article).first()
        if existing_rating:
            existing_rating.rating = rating_value 
            existing_rating.save()
            messages.success(request, 'Your rating has been updated!')
        else:
            Rating.objects.create(user=request.user, article=article, rating=rating_value)
            messages.success(request, 'Thank you for rating the article!')

        return redirect('catalog')  
    return redirect('login')  