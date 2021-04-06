from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.
def index(request):
    # images = Image.get_all_images()
    # locations = Location.objects.all()
    title = 'O_world'
    return render(request, 'index.html', )
