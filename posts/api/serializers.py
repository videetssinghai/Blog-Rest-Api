from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from posts.models import Post
from comments.api.serializers import CommentSerializer
from comments.models import Comment

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
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'comments'
        ]

    def get_comments(self,obj):
        content_type = obj.get_content_type
        object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs,many=True).data
        return comments




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


