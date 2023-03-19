from rest_framework import serializers

from posts.models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    """Serializer for post."""

    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    votes = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'user', 'user_id', 'votes','created']
    
    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()

class VoteSerializer(serializers.ModelSerializer):
    """Serializer for voter."""

    class Meta:
        model = Vote
        fields = ['id']