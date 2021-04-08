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


def review_list(request):
    latest_review_list = Review.objects.all()
    context = {'latest_review_list':latest_review_list}
    return render(request, 'review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.profile_Id = request.user.id
            profile.save()
        return redirect('index')

    else:
        form = NewProfileForm()
    return render(request, 'edit_profile.html', {"form": form})

    def get_object(self):
        return self.request.user



@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.editor = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})


@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.profile_Id = request.user.id
            profile.save()
        return redirect('profile')
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})   



# class UserEditView(generic.UpdateView):
#     form_class = NewProjectForm
#     template_name = 'edit_profile.html'
#     success_url = reverse_lazy('profile')

#     def get_object(self):
#         return self.request.user

def search_projects(request):

    # search for a user by their username
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any person"
        return render(request, 'search.html', {"message": message})






