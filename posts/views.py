from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm

# Create your views here.

# def post_list(request):
#     data = Post.objects.all  #get all posts from db             :Query
#     context = {'posts':data} #                                  :context
#     return render(request,'posts/post_list.html',context)#      :template

# Class Based View CBV::
from django.views.generic import ListView,DetailView
class PostList(ListView):               #context: model_list,object_list
    model = Post                        #Template: model_action-->post_list

# def post_detail(request,post_id):
#     data = Post.objects.get(id = post_id)
#     context = {'posts':data}
#     return render (request,'posts/post_detail .html',context) 

class PostDetail(DetailView):
    model = Post
    
    
    
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