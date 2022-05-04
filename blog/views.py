from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Post
# Create your views here.
def home(request):
    #load all the post from db()
    posts=Post.objects.all()[:11]
    cats=Category.objects.all
    
    return render(request,'home.html',{'posts':posts,'cats':cats})

def post(request,url):
    post=Post.objects.get(url=url)
    cats=Category.objects.all
    print(post)
    return render(request,'post.html',{'post':post,'cats':cats})

def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,'category.html',{'cat':cat,'posts':posts})

