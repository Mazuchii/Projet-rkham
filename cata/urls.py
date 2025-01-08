from django.urls import path, include
from . import views
from django.conf import settings
urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('', views.index1, name="index1"),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name="about"),
    path("add_comment/", views.add_comment, name="add_comment"),
]
