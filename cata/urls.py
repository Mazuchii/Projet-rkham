from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('', views.index1, name="index1"),
    path('', views.index, name="index"),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name="about"),
    path("add_comment/", views.add_comment, name="add_comment"),
]
