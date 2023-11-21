from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def mainPage(request):
    context = {}
    return render(request, 'sitePages/mainPage.html', context)

def postList(request):
    posts = Post.objects.all()
    return render(request, 'sitePages/postList.html', {'posts': posts})

def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'sitePages/postDetail.html', {'post': post})

def postEdit(request):
    context = {}
    return render(request, 'sitePages/postEdit.html', context)

def postForm(request):
    if request.method == 'POST':
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            # Processar os dados do formulário
            # ...
            formulario.save()
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