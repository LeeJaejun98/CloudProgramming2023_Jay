from django.shortcuts import render
from .models import Post, Category, Tag
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

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()

        return context


def single_post_page(request, post_num):
    post = Post.objects.get(pk=post_num)
    return render(request,
                  'blog/post_detail.html',
                  {'post': post}
                  )


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()

        return context


def categories_page(request, slug):
    if slug == 'no-category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context = {
        'category': category,
        'categories': Category.objects.all(),
        'post_list': post_list,
        'no_category_count': Post.objects.filter(category=None).count()

    }
    return render(request, 'blog/post_list.html', context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    context = {
        'tag': tag,
        'category': Category.objects.all(),
        'post_list': post_list,
        'no_category_count': Post.objects.filter(category=None).count()

    }
    return render(request, 'blog/post_list.html', context)