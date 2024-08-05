from rest_framework import serializers
from events.models import Event
from favorites.models import Favorite
from attendances.models import Attendance
from django.utils import timezone

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    event_date = serializers.DateTimeField(format='%d %b %Y %H:%M')
    favorite_id = serializers.SerializerMethodField()
    attendance_id = serializers.SerializerMethodField()
    attendance_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    def validate_event_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError('The event date cannot be in the past.')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_favorite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favorite = Favorite.objects.filter(owner=user, event=obj).first()
            return favorite.id if favorite else None
        return None

    def get_attendance_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attendance = Attendance.objects.filter(owner=user, event=obj).first()
            return attendance.id if attendance else None
        return None

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'description', 'event_date', 'event_image',
            'favorite_id', 'attendance_id', 'attendance_count',
            'comments_count'
        ]
