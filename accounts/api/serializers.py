from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from posts.models import Post
from django.contrib.auth import get_user_model




User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User

        fields =[
            'username',
            'password',
            'email'
        ]


        extra_kwargs = {"password":{"write_only":True}}