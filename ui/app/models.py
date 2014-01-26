#coding: utf-8
from django.db import models

class Photo(models.Model):
    url = models.TextField()