from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    event_title = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'event', 'event_title', 'created_at', 'updated_at', 'content'
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_event_title(self, obj):
        return obj.event.title if obj.event else None

class CommentDetailSerializer(CommentSerializer):
    event = serializers.ReadOnlyField(source='event.id')