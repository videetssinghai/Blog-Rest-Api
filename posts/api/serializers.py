from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
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
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'user',
            'content',
            'publish',
        ]

    def get_user(self,obj):
        return str(obj.user.username)


