from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from posts.models import Post



class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
         #  'slug',
            'content',
            'publish',
        ]

class PostDetailsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
    )

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'user',
            'content',
            'publish',
        ]
