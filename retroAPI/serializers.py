from django.contrib.auth.models import User, Group
from rest_framework import serializers
from retroAPI.models import Team, Retro

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'groups')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)

class RetroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retro
        field = ('title',)
