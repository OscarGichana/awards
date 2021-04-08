# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-04-08 08:11
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_moringamerch'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardsProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('pic', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='pic')),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=300)),
            ],
        ),
    ]