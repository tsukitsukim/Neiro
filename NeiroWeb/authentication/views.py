from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import *
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserAPIUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


'''
class UserAPIView(APIView):
    def get(self, request):
        w = User.objects.all()
        return Response({'get': UserSerializer(w, many=True).data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT is not allowed"})

        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response({"error": "Account does not exist"})

        serializer = UserSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
'''