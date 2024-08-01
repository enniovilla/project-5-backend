from django.db import IntegrityError
from rest_framework import serializers
from attendances.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    event_title = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = ['id', 'created_at', 'owner', 'event', 'event_title']

    def get_event_title(self, obj):
        return obj.event.title if obj.event else None

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': "You've already done this"
            })