from django.contrib.auth.models import User, Group
from rest_framework import serializers
from retroAPI.models import Team

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'groups')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        field = ('id', 'name')
