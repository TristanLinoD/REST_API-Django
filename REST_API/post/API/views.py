from rest_framework.viewsets import ModelViewSet
from post.models import Post
from .serializers import PostSerializer

class PostApiView(ModelViewSet):
  serializer_class = PostSerializer# Los datos que nos tiene que devolver 
  queryset = Post.objects.all()