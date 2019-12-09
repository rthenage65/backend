from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):

    _post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('created', 'comment', 'name', "_post")