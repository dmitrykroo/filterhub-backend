from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class PostDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
