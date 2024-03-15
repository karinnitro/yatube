from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "posts/index.html")
def group_posts(request, slug):
    if slug == "pomidor":
        return HttpResponse(f'<h2>Пост {slug}</h2><img src="https://foodcity.ru/storage/products/October2018/tFVuCnmXrEh4rWqkH3Gx.jpg"></img>')
    else:
        return HttpResponse(f'<h2>Пост {slug}</h2><img src="https://i.pinimg.com/564x/d1/b9/07/d1b907a965a32a7a3003043d507255d1.jpg"</img>')
    