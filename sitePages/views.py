from django.shortcuts import render

def mainPage(request):
    context = {}
    return render(request, 'sitePages/mainPage.html', context)

def postList(request):
    context = {}
    return render(request, 'sitePages/postList.html', context)

def postDetail(request):
    context = {}
    return render(request, 'sitePages/postDetail.html', context)

def postEdit(request):
    context = {}
    return render(request, 'sitePages/postEdit.html', context)

def postForm(request):
    context = {}
    return render(request, 'sitePages/postForm.html', context)