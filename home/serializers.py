from rest_framework import serializers
from home.models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'

class GameSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Game
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    played = GameSerializer(many=True)
    likes = GameSerializer(many=True)
    password=serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            login_id = validated_data['login_id'],
            nickname = validated_data['nickname']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields="__all__"


class PublichserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherGame
        fields='__all__'

class Comment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields='__all__'

