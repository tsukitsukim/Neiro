from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import User


class UserModel:
    def __init__(self, name, username):
        self.name = name
        self.username = username


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    username = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.username = validated_data.get("username", instance.username)
        instance.save()
        return instance
