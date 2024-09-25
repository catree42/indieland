from rest_framework import serializers
from home.models import *
import re
from rest_framework.exceptions import ValidationError


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)

    class Meta:
        model = Game
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True,
                                      label="Confirm Password")

    def validate_username(self, value):
        if len(value) < 6 or not value.isalnum() or not value.isascii():
            raise ValidationError(
                "Username must be at least 6 characters long and contain only English letters and numbers."
            )
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise ValidationError(
                "Password must be at least 6 characters long.")
        if not re.search(r"[A-Za-z]", value):
            raise ValidationError("Password must contain at least one letter.")
        if not re.search(r"\d", value):
            raise ValidationError("Password must contain at least one number.")
        return value

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"],
                                   email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]


class PublichserGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublisherGame
        fields = "__all__"


class Comment(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
