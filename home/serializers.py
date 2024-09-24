from rest_framework import serializers
from home.models import User, Game, Tag

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['login_id','password','nickname']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields=[]