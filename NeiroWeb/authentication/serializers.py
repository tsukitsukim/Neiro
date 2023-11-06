import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import User


class UserModel:
    def __init__(self, name, username, icon):
        self.name = name
        self.username = username
        self.icon = icon


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


'''
def encode():
    model = UserModel('Plizik', 'lovestea', "url", "2007.06.01")
    model_sr = UserSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"name":"test","username":"zzz"')
    data = JSONParser().parse(stream)
    serializer = UserSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)
'''