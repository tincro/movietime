from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.
def index(request):

    movies = Movie.objects.all()
    context = {"movieList": movies}

    return render(request, 'shows/index.html', context)