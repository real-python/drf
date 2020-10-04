# django
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Q
from .models import *
from .serializers import *
from django.contrib.auth.models import User
# rest_framework
from rest_framework import routers, serializers, viewsets, status
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView


class UserViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class = SerialalzerForViewset


# Only Post
class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class CreateUserDetails(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
