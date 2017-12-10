from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(User, related_name='team_members')
    def __str__(self):
        return self.name

class Retro(models.Model):
    title = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    current = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class RetroItem(models.Model):
    title = models.CharField(max_length=100)
    retro = models.ForeignKey(Retro, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey('Category', null=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255, null=True)
    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    organization = models.ForeignKey('Organization', null=True)