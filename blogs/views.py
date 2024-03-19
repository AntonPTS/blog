from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """Домашняя страница приложения Blog"""
    return render(request, 'blogs/index.html')

@login_required
def blog_posts(request):
    blog_posts = BlogPost.objects.order_by('date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/blog_posts.html', context)

@login_required
def blog_post(request, blog_id):
    blog_post = BlogPost.objects.get(id=blog_id)
    context = {'blog_post': blog_post}
    return render(request, 'blogs/blog_post.html', context)

@login_required
def edit_blog_post(request, blog_id):
    """Редактирует существующий блог-пост."""
    blog_post = BlogPost.objects.get(id=blog_id)
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущего блог-поста.
        form = BlogPostForm(instance=blog_post)
    else:
        # Отправка данных POST; обработать данные.
        form = BlogPostForm(instance=blog_post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_post', blog_id=blog_id)
    context = {'blog_post': blog_post, 'form': form}
    return render(request, 'blogs/edit_blog_post.html', context)

@login_required
def new_blog_post(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = BlogPostForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.owner = request.user
            new_blog_post.save()
            return redirect('blogs:blog_posts')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'blogs/new_blog_post.html', context)
