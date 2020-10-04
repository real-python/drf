from rest_framework import serializers, fields
from .models import *
from django.contrib.auth.models import User


# router viewset example
class SerialalzerForViewset(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


# Only User Create
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwarg = {'password': {'write_only': True}}
    
    def create(self, validate_data):
        print("validate_data :", validate_data)
        user = User(
            email=validate_data['email'],
            username=validate_data['username']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user


# -------------------- One To One ---------------------
class UserDetailSerializrs(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = ['phone']

class UserSerializer(serializers.ModelSerializer):
    userdetail = UserDetailSerializrs()
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'userdetail']
        extra_kwarg = {'password': {'write_only': True}}

    def create(self, validate_data):
        userdetail_data = validate_data.pop('userdetail')
        user = User.objects.create(**validate_data)
        user.set_password(validate_data['password'])
        UserDetail.objects.create(user=user, **userdetail_data)
        return user


        
        
        
         
    



