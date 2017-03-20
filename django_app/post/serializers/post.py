from rest_framework import permissions
from rest_framework import serializers

from member.serializers import UserSerializer
from post.models import Post
from post.serializers.post_photo import PostPhotoSerializer
from utils.pagination import PostPagination

__all__ = (
    'PostSerializer',
)

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    postphoto_set = PostPhotoSerializer(many=True, read_only=True)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = PostPagination

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'created_date',
            'postphoto_set',
        )
        read_only_fields = (
            'created_date',
        )