from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Group, Post
from django.shortcuts import redirect

def authorized_only(func):
    def check_user(request, *args, kwargs):
        if request.user.is_authenticated:
            return func(request, *args, *kwargs)
        return redirect('/auth/login/')
    return check_user


def index(request):
    post_list = Post.objects.order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title' : 'Последние обновления на сайте',
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    title = 'Записи группы '
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title + group.title,
        'posts': posts,
        'description': group.description,
    }
    return render(request, 'posts/group_list.html', context)

