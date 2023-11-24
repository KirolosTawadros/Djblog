from .models import Post

from django.views.generic import ListView,DetailView


class PostList(ListView):               #context: model_list,object_list
    model = Post                        #Template: model_action-->post_list

class PostDetail(DetailView):
    model = Post