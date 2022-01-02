"""定义learning_logs的URL模式"""
from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path('index/', views.index, name='index/'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics/')
]
