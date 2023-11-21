from django.shortcuts import render, get_object_or_404, redirect
from .models import post
from .forms import PostForm

def mainPage(request):
    context = {}
    return render(request, 'sitePages/mainPage.html', context)

def postList(request):
    posts = post.objects.all()
    return render(request, 'sitePages/postList.html', {'posts': posts})

def postDetail(request):
    postagem = get_object_or_404(post)
    return render(request, 'sitePages/postDetail.html', {'postDetail': postagem})

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