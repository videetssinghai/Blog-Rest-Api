from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from posts.models import Post
from comments.models import Comment


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
         #   'content_object',
            'parent',
            'content',
        ]
