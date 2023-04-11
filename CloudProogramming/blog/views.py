from django.shortcuts import render, redirect
from .models import Post, Category, Tag
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView


# 정적 렌더링
# def index(request):
# posts = Post.objects.all().order_by('-pk')
#  return render(request, 'blog/post_list.html',
#                 {'posts': posts})
#   -> class based view 만들기 때문에 필요없음

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload', 'category', 'tag']

    template_name = 'blog/post_update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object().author == request.user:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionError


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):       # 사용자에게 정보를 받아오는 페이지 + 페이지에 들어있는 홈의 정보 가져오기
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload', 'category', 'tag']  # 7개만 받기

    def test_func(self):
        return self.request.is_superuser or self.request.is_staff

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()

        return context

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')


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
    return render(request, 'blog/post_list.html', context)  # function based view