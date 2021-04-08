from __future__ import unicode_literals
from django.db import models
import datetime as dt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver
from django.db.models.signals import (post_save,pre_save,)
# from PIL import Image
from django.core.files import File
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
import numpy as np
from django.db.models import Avg, Max, Min

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 60,null=True,blank=True)
    last_name = models.CharField(max_length = 60,null=True,blank=True)
    pic = CloudinaryField('pic',null=True) 
    bio = models.TextField(null=True,blank=True)
    likes = models.IntegerField(default=0)
    email = models.EmailField(null=True)
    phone_number = PhoneNumberField(null=True)

    def get_total_likes(self):
        return self.likes.user.count()

    @classmethod
    def update_profile(cls, id, email, phone_number, first_name, last_name, bio, pic):
        profile = cls.objects.filter(id = id).update(pic = pic, id = id, first_name=first_name, last_name=last_name,bio=bio,phone_number=phone_number, email=email)
        
        return update


    def __str__(self):
        return str(self.user.username)
    class Meta:
        ordering = ['first_name']
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()


def create_profile(sender, instance, created, **kwargs):
    if created: Profile.objects.create(user=instance)

post_save.connect(create_profile, sender = User)


class Project(models.Model):
    title = models.CharField(max_length = 60)
    pic = CloudinaryField('pic',null=True) 
    description = models.TextField()
    link = models.URLField(max_length = 300)

    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def update_project(cls, id, caption):
        update = cls.objects.filter(id = id).update(description = description)
        # return update

    @classmethod
    def get_all_projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_project_by_id(cls,id):
        project = cls.objects.filter(id= id).all()
        return project

    def average_design(self):
        design_ratings = list(map(lambda x: x.design_rating, self.reviews.all()))
        return np.mean(design_ratings)

    def average_usability(self):
        usability_ratings = list(map(lambda x: x.usability_rating, self.reviews.all()))
        return np.mean(usability_ratings)

    def average_content(self):
        content_ratings = list(map(lambda x: x.content_rating, self.reviews.all()))
        return np.mean(content_ratings)


    def get_total_likes(self):
        return self.likes.users.count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']



class Review(models.Model):
    RATING_CHOICES = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8'),(9, '9'),(10, '10'),)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    design_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.IntegerField(choices=RATING_CHOICES, default=0)

    def save_comment(self):
        self.save()

    def get_comment(self, id):
        comments = Review.objects.filter(project_id =id)
        return comments

    def __str__(self):
        return self.comment


class MoringaMerch(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 60,null=True,blank=True)
    pic = CloudinaryField('pic',null=True) 
    bio = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True)

class AwardsProject(models.Model):
    title = models.CharField(max_length = 60)
    pic = CloudinaryField('pic',null=True) 
    description = models.TextField()
    link = models.URLField(max_length = 300)
