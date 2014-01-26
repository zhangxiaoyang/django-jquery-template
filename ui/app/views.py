#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import Photo
import json

def index(request):
    return render(request, 'index.html', locals())
def photos(request):
    return render(request, 'photos.html', locals())
def query(request):
    photos = [ photo.url for photo in Photo.objects.all() ]
    return HttpResponse(json.dumps(photos))
