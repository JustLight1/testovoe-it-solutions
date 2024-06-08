from rest_framework import generics

from posts.models import Post
from src import settings

from .serializers import PostSerializer


class PostsList(generics.ListAPIView):
    queryset = Post.objects.all().order_by(
        'position')[:settings.MAX_POSTS_COUNT]
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
