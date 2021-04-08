from django.shortcuts import render,redirect,get_object_or_404,reverse
import datetime as dt
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView
from django import forms
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,Review
from .forms import ReviewForm,NewProjectForm,NewProfileForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  MoringaMerch,AwardsProject
from .serializer import MerchSerializer,ProjectSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly



# Create your views here.
def index(request):
    projects = Project.get_all_projects()
    # locations = Location.objects.all()
    title = 'O_world'
    return render(request, 'index.html', {"projects":projects})


@login_required(login_url='/accounts/login/')
def profile(request):
    title = 'O_world'
    user = request.user
    return render(request, 'profile.html')



def project(request, id):

    try:
        project = Project.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Review.get_comment(Review, id)
    latest_review_list=Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()

    else:
        form = ReviewForm()

        # return HttpResponseRedirect(reverse('image', args=(image.id,)))

    return render(request, 'image.html', {"project": project,
                                          'form':form,
                                          'comments':comments,
                                          'latest_review_list':latest_review_list})




