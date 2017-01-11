from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView)
from comments.models import Comment
from .serializers import (
UserCreateSerializer)
from rest_framework.permissions import (
AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
)
from django.contrib.auth import get_user_model






User = get_user_model()



class UserCreateApiVIew(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()