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


def encode():
    model = UserModel('Plizik', 'lovestea')
    model_sr = UserSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)
