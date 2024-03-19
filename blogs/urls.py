"""Определяет схемы URL для Blog."""

from django.urls import path, include
from . import views

app_name = 'blogs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    path('blog_posts/', views.blog_posts, name='blog_posts'),
    path('blog_post/<int:blog_id>/', views.blog_post, name='blog_post'),
    path('edit_blog_post/<int:blog_id>/', views.edit_blog_post, name='edit_blog_post'),
    path('new_blog_post/', views.new_blog_post, name='new_blog_post')
]