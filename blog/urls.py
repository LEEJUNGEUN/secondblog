from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('newblog/', views.blogpost, name='newblog'),
    path('update/<int:pk>', views.update, name="update"), #여러개의 글 중 특정 글을 선택해서 수행 

]
