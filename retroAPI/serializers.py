from django.contrib.auth.models import User, Group
from rest_framework import serializers
from retroAPI.models import Team, Retro, RetroItem, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    class Meta:
        model = Team
        fields = ('id', 'name', 'owner', 'description', 'members')

class RetroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retro
        fields = ('title', 'team', 'id')

class RetroItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= RetroItem
        fields = ('title', 'retro', 'category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')
