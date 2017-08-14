from __future__ import unicode_literals
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Retro(models.Model):
    title = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title

class RetroItem(models.Model):
    title = models.CharField(max_length=100)
    def __str__(arg):
        return self.title
