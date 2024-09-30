from rest_framework import serializers
from home.models import *
import re
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Game
        fields = "__all__"



class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True, label='비밀번호 확인')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')  # 비밀번호 확인 필드는 저장하지 않음
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # 비밀번호 해싱
        user.save()
        return user
    

# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, attrs):
#         username = attrs.get('username')
#         password = attrs.get('password')

#         if username and password:
#             user = authenticate(request=self.context.get('request'), username=username, password=password)
#             if not user:
#                 raise serializers.ValidationError('사용자 이름 또는 비밀번호가 잘못되었습니다.')
#         else:
#             raise serializers.ValidationError('사용자 이름과 비밀번호를 입력해야 합니다.')

#         attrs['user'] = user
#         return attrs

# serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError("잘못된 사용자 이름 또는 비밀번호입니다.")
        attrs['user'] = user
        return attrs



class PublichserGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublisherGame
        fields = "__all__"


class Comment(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
