from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView)
from posts.models import Post
from .serializers import PostListSerializer, PostDetailsSerializer, PostCreateUpdateSerializer
from rest_framework.permissions import (
AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
)
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
OrderingFilter,
)

from .pagination import PostLimitOffsetPaginnation, PostPageNumberPagniation









class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter]
    search_fields = [ 'title' , 'content','user__first_name',]
    pagination_class = PostPageNumberPagniation

    def get_queryset(self,*args,**kwargs):
        query = self.request.GET.get("q")
        queryset_list =  Post.objects.all()
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list



class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer
    lookup_field = 'slug'
