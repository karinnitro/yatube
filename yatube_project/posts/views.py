from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Group, Post

# Create your views here.


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'title': "Последние обновления на сайте",
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    title = 'Записи групп'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': group.title,
        'posts': posts,
        'description': group.description,
    }
    return render(request, 'posts/group_list.html', context)
