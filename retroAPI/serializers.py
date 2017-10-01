from django.contrib.auth.models import User, Group
from rest_framework import serializers
from retroAPI.models import Team, Retro, RetroItem, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'groups')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'owner', 'description')

class RetroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retro
        fields = ('title', 'team', 'id', 'url')

class RetroItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= RetroItem
        fields = ('title', 'retro', 'category', 'url')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')
