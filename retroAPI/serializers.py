from django.contrib.auth.models import User, Group
from rest_framework import serializers
from retroAPI.models import Team, Retro, RetroItem, Category, Organization, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'organization')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        print("inside UserSerializer")
        print(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    class Meta:
        model = Team
        fields = ('id', 'name', 'owner', 'description', 'members')

class RetroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retro
        fields = ('title', 'team', 'id', 'current')

class RetroItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= RetroItem
        fields = ('title', 'retro', 'category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description', 'id')

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('name', 'id')

    def create(self, validated_data):
        organization = super(Organization, self).create(validated_data)
        organization.set_name(validated_data['company_name'])
        organization.save()
        return organization
