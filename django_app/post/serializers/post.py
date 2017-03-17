from rest_framework import serializers

from member.serializers import UserSerializer
from post.models import Post


__all__ = (
    'PostSerializer',
)

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'created_date',
        )
        read_only_fields = (
            'created_date',
        )