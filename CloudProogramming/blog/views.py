from django.shortcuts import render
from .models import Post


# 정적 렌더링
def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(request, 'blog/index.html',
                  {'posts': posts})
