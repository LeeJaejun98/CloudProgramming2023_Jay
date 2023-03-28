from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# 정적 렌더링
# def index(request):
# posts = Post.objects.all().order_by('-pk')
#  return render(request, 'blog/post_list.html',
#                 {'posts': posts})
#   -> class based view 만들기 때문에 필요없음
class PostList(ListView):
    model = Post
    ordering = '-pk'  # 내림차순으로 정렬해주기 위해


def single_post_page(request, post_num):
    post = Post.objects.get(pk=post_num)
    return render(request,
                  'blog/post_detail.html',
                  {'post': post}
                  )


class PostDetail(DetailView):
    model = Post
