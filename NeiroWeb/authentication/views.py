from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserAPIView(APIView):
    def get(self, request):
        lst = User.objects.all().values()
        return Response({'get': list(lst)})

    def post(self, request):
        post_new = User.objects.create(
            name=request.data['name'],
            username=request.data['username'],
        )
        return Response({'post': model_to_dict(post_new)})

#class UserAPIView(generics.ListAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer