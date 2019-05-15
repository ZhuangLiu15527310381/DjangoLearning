from django.shortcuts import render, redirect  # 使用简写的redirect
from django.http import request
from django.http import HttpResponse, HttpResponseRedirect
from myapp1.models import BlogPost
from datetime import datetime


# Create your views here.
# 1、定义视图函数
# 2、进行url配置，建立url地址和视图的对应关系
def index(request):
    posts = BlogPost.objects.all().order_by('-timestamp')
    return render(request, "index.html", {"posts": posts})


def delete(request, bid):
    blog = BlogPost.objects.get(id=bid)
    blog.delete()
    return redirect('/blog')


def create(request):
    title = request.POST.get("title")
    author = request.POST.get("author")
    body = request.POST.get("body")
    blog = BlogPost()
    blog.title = title
    blog.author_name = author
    blog.body = body
    blog.timestamp = datetime.now()
    blog.save()
    return redirect('/blog')


def direct(request, bid):
    blog = BlogPost.objects.get(id=bid)
    return render(request, 'Update.html',{'blog':blog})

def update(request,bid):
    blog = BlogPost.objects.get(id=bid)
    title = request.POST.get("title")
    author = request.POST.get("author")
    body = request.POST.get("body")
    blog.title = title
    blog.author_name = author
    blog.body = body
    blog.timestamp = datetime.now()
    blog.save()
    return redirect('/blog')

def page_not_found(request):

    return render(request, '404.html')
