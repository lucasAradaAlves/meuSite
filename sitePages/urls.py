from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('postList/', views.postList, name='postList'),
    path('postDetail/', views.postDetail, name='postDetail'),
    path('postEdit/', views.postEdit, name='postEdit'),
    path('postForm/', views.postForm, name='postForm'),
    path('posts/', views.postList, name='postList'),
    path('post/<int:pk>/', views.postDetail, name='postDetail'),
    path('post/<int:pk>/delete/', views.postDeleteConfirm, name='postDeleteConfirm'),
    path('post/<int:pk>/delete/confirm/', views.postDelete, name='postDelete'),
    path('post/<int:pk>/edit/', views.postEdit, name='postEdit'),
    path('post/<int:pk>/comment/', views.createComment, name='createComment'),
]