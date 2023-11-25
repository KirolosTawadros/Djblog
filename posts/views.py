from django.shortcuts import render , redirect
from .models import Post , Comment
from .forms import PostForm,CommentForm

# Create your views here.

def post_list(request):
    data = Post.objects.all  #get all posts from db             #:Query
    context = {'posts':data}                                    #:context
    return render(request,'posts/post_list.html',context)       #:template


def post_detail(request,pk):
    data = Post.objects.get(id = pk)
    comments = Comment.objects.filter(post=data)


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()        
        
        
    context = {'posts':data,
            'comments':comments,
            'form':form,
            }
    
    return render (request,'posts/post_detail.html',context) 



def create_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auth = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm()
    
    return render(request,'posts/new.html',{'form':form})



def edit_post(request,pk):
    post = Post.objects.get(id = pk)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auth = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm(instance=post)
    
    return render(request,'posts/edit.html',{'form':form})


def delete_post(request,pk):
    post = Post.objects.get(id = pk)
    post.delete()
    
    return redirect('/posts/')
