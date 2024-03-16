from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'base.html'
    title = 'Главная страница'
    content = 'Это главная страница проекта Yatube'
    context= {
        'title': title,
        'content': content
    }
    return render(request, template, context)
def group_posts(request, slug):
    template = 'base.html'
    title = 'Записи групп'
    content = 'Здесь будет информация о группах проекта Yatube'
    context= {
        'title': title,
        'content': content
    }
    return render(request, template, context)