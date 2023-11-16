from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    data = Post.objects.all  #get all posts from db

    context = {
        'posts':data
    }
    return render(request,'posts/post_list.html',context)


def post_detail(request,post_id):
    data = Post.objects.get(id = post_id)
    context = {
        'posts':data
    }
    
    return render (request,'posts/post_details.html',context) 