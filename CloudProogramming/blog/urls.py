#url congfig for blog
from . import views     #. = 현재 파일에서의 views를 쓰겠다
from django.urls import path, include

urlpatterns = [

    path('', views.PostList.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('post_update/<int:pk>/', views.PostUpdate.as_view()),
    #path('', views.index),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.categories_page),
    path('tag/<str:slug>/', views.tag_page)
]
