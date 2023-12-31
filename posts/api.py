from .models import Post
from .serializers import Postserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def post_list_api(request):
    posts = Post.objects.all()
    data = Postserializer(posts,many= True).data
    return Response ({'data':data})


@api_view(['GET'])
def post_detail_api(request):
    posts = Post.objects.all()
    data = Postserializer(posts,many= True).data
    return Response ({'data':data})