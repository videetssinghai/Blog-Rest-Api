from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView)
from posts.models import Post
from .serializers import PostListSerializer, PostDetailsSerializer, PostCreateUpdateSerializer



class PostCreateUpdateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer
    lookup_field = 'slug'
