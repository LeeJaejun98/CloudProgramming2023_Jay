#url congfig for blog
from . import views     #. = 현재 파일에서의 views를 쓰겠다
from django.urls import path, include
urlpatterns = [
    path('', views.index),
    path('<int:post_num>/', views.single_post_page),
]
