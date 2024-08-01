from rest_framework import serializers
from favorites.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorite
        fields = ['id', 'created_at', 'owner', 'event']