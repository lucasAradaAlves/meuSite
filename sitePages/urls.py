from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('postList/', views.postList, name='postList'),
    path('postDetail/', views.postDetail, name='postDetail'),
    path('postEdit/', views.postEdit, name='postEdit'),
    path('postForm/', views.postForm, name='postForm'),
]