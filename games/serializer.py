from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'player', 'title', 'description', 'created_at', 'updated_at')
        model = Game