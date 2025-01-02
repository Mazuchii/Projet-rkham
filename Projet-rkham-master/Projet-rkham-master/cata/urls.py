from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('', views.index1, name="index1"),
    path('rate_article/<int:article_id>/', views.rate_article, name='rate_article'),
]
