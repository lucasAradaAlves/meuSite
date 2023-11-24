from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def mainPage(request):
    context = {}
    return render(request, 'sitePages/mainPage.html', context)

def postList(request):
    posts = Post.objects.all()
    return render(request, 'sitePages/postList.html', {'posts': posts})

@login_required
def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-pub_date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.pub_date = timezone.now()
            comment.save()
            return redirect('postDetail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'sitePages/postDetail.html', {'post': post, 'comments': comments, 'form': form})

def postEdit(request):
    context = {}
    return render(request, 'sitePages/postEdit.html', context)

@login_required
def postForm(request):
    if request.method == 'POST':
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.author = request.user
            post.time = timezone.now()
            post.save()
            formulario.save_m2m()
            return redirect('postList')
    else:
        formulario = PostForm()
    return render(request, 'sitePages/postForm.html', {'formulario': formulario})

def postDeleteConfirm(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'sitePages/postDeleteConfirm.html', {'post': post})

def postDelete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('postList')

@login_required
def postEdit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('postDetail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'sitePages/postEdit.html', {'form': form, 'post': post})

@login_required
def createComment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.pub_date = timezone.now()
            comment.save()
            return redirect('postDetail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'sitePages/createComment.html', {'form': form, 'post': post})

def categoryList(request):
    categories = Category.objects.all()
    return render(request, 'sitePages/categoryList.html', {'categories': categories})

def categoryDetail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(categories=category)
    return render(request, 'sitePages/categoryDetail.html', {'category': category, 'posts': posts})

def getPostsInCategory(category_id):
    try:
        category = Category.objects.get(id=category_id)
        postsInCategory = Post.objects.filter(categories=category)
        return postsInCategory
    except Category.DoesNotExist:
        return None