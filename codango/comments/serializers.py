from rest_framework import serializers

from models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Comment Serializer"""

    class Meta:
        model = Comment
        fields = ('id', 'author', 'resource', 'content', 'date_created',
                  'date_modified')

        read_only_fields = ('date_created', 'date_modified')
