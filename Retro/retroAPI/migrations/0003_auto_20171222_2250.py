# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retroAPI', '0002_organization_teams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='teams',
        ),
        migrations.AddField(
            model_name='team',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_organization', to='retroAPI.Organization'),
        ),
    ]
