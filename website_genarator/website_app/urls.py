from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('add-website/', views.add_website, name='add_website'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-book/', views.add_book, name='add_book'),
    path('add-review/', views.add_review, name='add_review'),]