# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-04-06 19:35
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=60, null=True)),
                ('pic', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='pic')),
                ('bio', models.TextField(blank=True, null=True)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('pic', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='pic')),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=60)),
            ],
        ),
    ]