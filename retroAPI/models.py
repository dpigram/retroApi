from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Retro(models.Model):
    title = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title

class RetroItem(models.Model):
    title = models.CharField(max_length=100)
    retro = models.ForeignKey(Retro, on_delete=models.CASCADE, null=True)
    def __str__(arg):
        return self.title
