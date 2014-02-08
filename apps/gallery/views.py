from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo


class GalleryListView(ListView):
    model = Photo
    context_object_name = 'photos'
