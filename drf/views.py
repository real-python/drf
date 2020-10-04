# django
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Q
from .models import *
from .serializers import *
from django.core.cache import cache #cache
# rest_framework
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
# swagger
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# custom Request & Response in swagger (APIView)
class CreateUSer(APIView):
    permission_classes = [AllowAny, ]
    response = openapi.Response(
        'response description', CustomResponseSerializers
    )
    @swagger_auto_schema(
        request_body = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='User Name'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User Email'),
            },
            required=['email'],
        ),
        responses = {
            status.HTTP_200_OK: CustomResponseSerializers
        } 
    )

    def post(self, request, format=None):
        name = request.data['name']
        email = request.data['email']
        print(name, email)
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Get & Post
class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Post only
class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Get Only
class UserListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Retrieve/Fetch only one data/record from database by id
class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Update one record from db by using id
class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [AllowAny, ]
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Delete one record from db by using id
class UserDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [AllowAny, ]
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer


# data Filtering
class FilterUser1(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer
    # Filtering on know params
    def get_queryset(self):
        return User.objects.filter(name='Jhon')
    """
        http://127.0.0.1:8000/api/filter1/
    """


# data Filtering
class FilterUser2(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer
    # Filtering on kwarg which we are getting from url
    def get_queryset(self):
        kwarg_url_value = self.kwargs['name']
        return User.objects.filter(name=kwarg_url_value)
    """
        http://127.0.0.1:8000/api/filter2/Jhon/
    """


class FilterUser3(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer
    # Filtering url query params
    def get_queryset(self):
        queryset = User.objects.all()
        q_value = self.request.query_params.get('name', 'None')
        if q_value is not None:
            queryset = queryset.filter(name=q_value)
        return queryset
    """
        http://127.0.0.1:8000/api/filter3/?name=Jhon
    """


class FilterUser4(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    """
        Note: pattern search work here 
        http://127.0.0.1:8000/api/filter4/?search=jh
    """


# FK relation
# Get and Post
class MusicianListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    # authentication_classes =[]  # to bypass security
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

class StudentListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = Student.objects.all()
    serializer_class = StudentSerialzers

# Get and Post
class AlbumListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


# Many To Many relation (Get & Post)
class PostCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = Post.objects.all()
    serializer_class = PostSerialzers
    """
        http://127.0.0.1:8000/api/post/  ----> Get method 
    """
