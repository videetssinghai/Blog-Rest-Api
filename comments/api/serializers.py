from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from posts.models import Post
from comments.models import Comment


class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'reply_count',
            'parent',
            'content',
        ]

    def get_reply_count(self,obj):
        if obj.is_parent:
            return obj.Children().count()
        return 0


class CommentChildSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'timestamp',
        ]

class CommentDetailSerializer(ModelSerializer):
    replies = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'replies',
            'content',
            'timestamp'
        ]

        read_only_fields =['content_type','replies']

    def get_replies(self,obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.Children(),many=True).data
        return None

